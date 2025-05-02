import json


class Database:
    def __init__(self, db_file='plates.json'):
        with open(db_file) as f:
            self.data = json.load(f)

    def is_plate_authorised(self, plate):
        print(f"Checking if plate is authorised...")
        return plate in self.data['plates']
