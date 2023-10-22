import cv2
import numpy as np

# Create a background subtractor object
fgbg = cv2.createBackgroundSubtractorMOG2()

# Load the video
cap = cv2.VideoCapture('IMG_3627.mov')

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Denoise the mask to reduce false positives
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

    # Draw contours around detected moving objects
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        # Calculate contour area
        area = cv2.contourArea(cnt)

        # Filter out small contours (likely shadows)
        if area > 100:  # Adjust this threshold as needed
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with the contours around moving objects
    cv2.imshow('Basketball Coaching App', frame)

    if cv2.waitKey(1) & 0xFF == 27: # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()