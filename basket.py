import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('IMG_3627.mov')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color range for the ball
    lower_ball = np.array([hue_lower, sat_lower, val_lower])
    upper_ball = np.array([hue_upper, sat_upper, val_upper])

    # Create a mask for the ball
    ball_mask = cv2.inRange(hsv, lower_ball, upper_ball)

    # Find the ball in the mask
    ball_contours, _ = cv2.findContours(ball_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in ball_contours:
        # Calculate contour area
        area = cv2.contourArea(cnt)
        # Filter out small contours
        if area > ball_area_threshold:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Use Hough Circle Transform to detect the hoop
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)

    # Display the frame with the ball and hoop highlighted
    cv2.imshow('Basketball Coaching App', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()