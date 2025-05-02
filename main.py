import warnings
from anpr.camera import Camera
from anpr.plate_detector import PlateDetector
from anpr.database import Database
from anpr.gate_controller import GateController


warnings.filterwarnings("ignore", message=".*pin_memory.*")


def main():
    camera = Camera()
    detector = PlateDetector()
    db = Database()
    gate = GateController()

    print("System ready. Scanning for vehicles...")

    # Skipping real capture for now, just using test image
    image = "test_plate.jpg"
    plate_text, confidence = detector.detect_plate(image)
    plate_text = plate_text.replace("'", "").replace(" ", "").upper()

    if plate_text:
        print(f"Detected plate: {plate_text} (Confidence: {confidence:.2f})")
        if db.is_plate_authorised(plate_text):
            gate.open()
            print("Gate opened.")
        else:
            print("Plate not recognised. Gate remains closed.")
    else:
        print("No plate detected.")


if __name__ == "__main__":
    main()
