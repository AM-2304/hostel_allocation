from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import csv
from models import GroupInfo, HostelInfo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hostel.db'
db = SQLAlchemy(app)
db.init_app(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/api/upload', methods=['POST'])
def upload_files():
    group_file = request.files['group_file']
    hostel_file = request.files['hostel_file']

    # Process group file
    group_data = []
    with group_file.stream as f:
        reader = csv.DictReader(f)
        for row in reader:
            group_data.append({
                'group_id': int(row['Group ID']),
                'members': int(row['Members']),
                'gender': row['Gender']
            })

    # Process hostel file
    hostel_data = []
    with hostel_file.stream as f:
        reader = csv.DictReader(f)
        for row in reader:
            hostel_data.append({
                'hostel_name': row['Hostel Name'],
                'room_number': int(row['Room Number']),
                'capacity': int(row['Capacity']),
                'gender': row['Gender']
            })

    # Save data to the database
    save_data_to_db(group_data, hostel_data)

    # Allocate rooms
    allocation = allocate_rooms(group_data, hostel_data)

    return jsonify({'allocation': allocation})

def save_data_to_db(group_data, hostel_data):
    # Save group data to the database
    for group in group_data:
        db_group = GroupInfo(
            group_id=group['group_id'],
            members=group['members'],
            gender=group['gender']
        )
        db.session.add(db_group)

    # Save hostel data to the database
    for hostel in hostel_data:
        db_hostel = HostelInfo(
            hostel_name=hostel['hostel_name'],
            room_number=hostel['room_number'],
            capacity=hostel['capacity'],
            gender=hostel['gender']
        )
        db.session.add(db_hostel)

    db.session.commit()

def allocate_rooms(group_data, hostel_data):
    allocation = []
    for group in group_data:
        # Find available rooms based on group size and gender
        available_rooms = [
            room for room in hostel_data
            if room['capacity'] >= group['members']
            and room['gender'] == group['gender']
        ]

        if available_rooms:
            # Allocate the group to the first available room
            room = available_rooms[0]
            allocation.append({
                'group_id': group['group_id'],
                'hostel_name': room['hostel_name'],
                'room_number': room['room_number'],
                'members_allocated': group['members']
            })

            # Update the available capacity of the room
            room['capacity'] -= group['members']
        else:
            # No available room found for the group
            allocation.append({
                'group_id': group['group_id'],
                'hostel_name': 'No Allocation',
                'room_number': 'N/A',
                'members_allocated': group['members']
            })

    return allocation

if __name__ == '__main__':
    app.run(debug=True)
