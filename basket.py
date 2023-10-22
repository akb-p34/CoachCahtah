import cv2
import numpy as np

# Create a VideoCapture object to read the video
cap = cv2.VideoCapture('IMG_3627.mov')

# Initialize the list of ball positions
ball_positions = []

# Define the boxes for scoring
x1=1595
y1=931
x2=1765
y2=930
x3=1625
y3=1125
x4=1725
y4=1100
hoop_box = (x1, y1, x2, y2)  # Define the coordinates for the hoop box
bottom_box = (x3, y3, x4, y4)  # Define the coordinates for the bottom box

# Loop until the end of the video
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Convert from BGR to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the range of orange color in HSV (for the ball)
        lower_orange = np.array([0, 60, 165])
        upper_orange = np.array([5, 255, 255])

        # Define the range of red color in HSV (for the hoop)
        lower_red = np.array([157,105,110])
        upper_red = np.array([215,72,73])

        # Threshold the HSV image to get only orange colors (for the ball)
        mask_orange = cv2.inRange(hsv_frame, lower_orange, upper_orange)

        # Threshold the HSV image to get only green colors (for the hoop)
        mask_green = cv2.inRange(hsv_frame, lower_red, upper_red)

        # Find contours in the mask (for the ball)
        contours_orange, _ = cv2.findContours(mask_orange.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find contours in the mask (for the hoop)
        contours_green, _ = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the largest contour, which should be the ball
        if len(contours_orange) > 0:
            largest_contour_orange = max(contours_orange, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour_orange)
            center = (int(x), int(y))

            # Append the center to the ball_positions list
            ball_positions.append(center)

            # Draw a circle around the detected ball
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)

        # Draw the scoring boxes
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Hoop box
        cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)  # Bottom box

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