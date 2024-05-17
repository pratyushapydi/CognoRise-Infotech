import cv2
import numpy as np
def decode_qr_code(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = detector.detectAndDecode(img)
    return data

image_path = "qr_code.png"
decoded_data = decode_qr_code(image_path)
print("Decoded data:", decoded_data)