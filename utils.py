from models import GroupInfo, HostelInfo

def allocate_rooms():
    # Implement the room allocation algorithm here
    # ...
    # Return the room allocation data
    return [
        {
            'group_id': 101,
            'hostel_name': 'Boys Hostel A',
            'room_number': 101,
            'members_allocated': 3
        },
        {
            'group_id': 102,
            'hostel_name': 'Girls Hostel B',
            'room_number': 202,
            'members_allocated': 4
        },
        # Add more allocation data
    ]
