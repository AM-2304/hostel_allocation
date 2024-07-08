from app import db

class GroupInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, nullable=False)
    members = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

class HostelInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostel_name = db.Column(db.String(50), nullable=False)
    room_number = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
