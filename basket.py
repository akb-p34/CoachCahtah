import cv2
import numpy as np

cap = cv2.VideoCapture('IMG_3627.mov')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Process the frame here
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()