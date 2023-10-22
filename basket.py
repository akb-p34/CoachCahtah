import cv2
import numpy as np

# Create a VideoCapture object to read the video
cap = cv2.VideoCapture('IMG_3627.mov')

# Initialize the list of ball positions
ball_positions = []

# Loop until the end of the video
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Convert from BGR to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the range of orange color in HSV
        lower_orange = np.array([0, 60, 165])
        upper_orange = np.array([5, 255, 255])

        # Threshold the HSV image to get only orange colors
        mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the largest contour, which should be the ball
        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
            center = (int(x), int(y))

            # Append the center to the ball_positions list
            ball_positions.append(center)

            # Draw a circle around the detected ball
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)

            # Draw a line connecting the ball positions
            for i in range(1, len(ball_positions)):
                cv2.line(frame, ball_positions[i - 1], ball_positions[i], (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Define 'q' as the exit button
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object
cap.release()

# Closes all the windows currently opened.
cv2.destroyAllWindows()