import cv2
import easyocr


class PlateDetector:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def detect_plate(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Failed to load image from: {image_path}")

        results = self.reader.readtext(image)
        if not results:
            return None, 0.0

        # Sort results left to right by bounding box x-coordinate
        results.sort(key=lambda x: x[0][0][0])

        # Combine detected texts
        plate_text = ''.join([text for _, text, _ in results])
        avg_confidence = sum(conf for *_, conf in results) / len(results)

        return plate_text, avg_confidence
