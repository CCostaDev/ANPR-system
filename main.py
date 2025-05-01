from anpr.camera import Camera
from anpr.plate_detector import PlateDetector
from anpr.database import Database
from anpr.gate_controller import GateController

def main():
    camera = Camera()
    detector = PlateDetector()
    db = Database()
    gate = GateController()

    print("System ready. Scanning for vehicles...")

    image = camera.capture()
    plate = detector.detect_plate(image)

    if plate:
        print(f"Detected plate: {plate}")
        if db.is_plate_authorised(plate):
            gate.open()
            print("Gate opened.")
        else:
            print("Plate not recognised. Gate remains closed.")
    else:
        print("No plate detected.")

if __name__ == "__main__":
    main()