from anpr.camera import Camera
from anpr.plate_detector import PlateDetector
from anpr.database import Database
from anpr.gate_controller import GateController

# T01 – Camera.capture() returns expected placeholder
def test_camera_capture_returns_placeholder():
    camera = Camera()
    result = camera.capture()
    assert result == "image_data"

# T02 – PlateDetector returns the correct mock plate
def test_plate_detector_returns_mock_plate():
    detector = PlateDetector()
    result = detector.detect_plate("image_data")
    assert result == "AB12CDE"

# T03 – Database returns True for authorised plate
def test_database_returns_true_for_authorised_plate():
    db = Database()
    assert db.is_plate_authorised("AB12CDE") is True

# T04 – Database returns False for unauthorised plate
def test_database_returns_false_for_unauthorised_plate():
    db = Database()
    assert db.is_plate_authorised("XYZ123") is False

# T05 – GateController prints expected message
def test_gate_controller_prints_gate_open_message(capfd):
    gate = GateController()
    gate.open()
    out, _ = capfd.readouterr()
    assert "Opening gate" in out

# T06 – Main flow (mocked) – simulate full logic manually
def test_full_flow_simulation():
    camera = Camera()
    detector = PlateDetector()
    db = Database()
    gate = GateController()

    image = camera.capture()
    plate = detector.detect_plate(image)

    if db.is_plate_authorised(plate):
        # If needed, simulate gate.open() or just assert logic
        result = True
    else:
        result = False

    assert result is True
