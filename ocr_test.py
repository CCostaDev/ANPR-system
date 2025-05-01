import easyocr

reader = easyocr.Reader(['en'])  # Load the English OCR model

image_path = 'test_plate.jpg'

print(f"Reading plate from {image_path}...")

results = reader.readtext(image_path)

for bbox, text, confidence in results:
    print(f"Detected: '{text}' (Confidence: {confidence:.2f})")
