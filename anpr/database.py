class Database:
    def __init__(self):
        # Simulated authorised plates list
        self.authorised_plates = ["AB12CDE", "XY99ZRT"]

    def is_plate_authorised(self, plate):
        print(f"Checking if {plate} is authorised...")
        return plate in self.authorised_plates
