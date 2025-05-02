import easyocr
import cv2

reader = easyocr.Reader(['en'])  # Load the English OCR model

image_path = 'test_plate.jpg'
image = cv2.imread(image_path)

print(f"Reading plate from {image_path}...")

results = reader.readtext(image)

for bbox, text, confidence in results:
    print(f"Detected: '{text}' (Confidence: {confidence:.2f})")
