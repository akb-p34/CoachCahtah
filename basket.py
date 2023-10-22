import cv2
import numpy as np

# Create a VideoCapture object to read the video
cap = cv2.VideoCapture('MadeShot.mov')
#cap = cv2.VideoCapture('MissedShot.mov')

# Initialize the list of ball positions
ball_positions = []

# Initialize the box conditions
touchHoopBox = False
touchBottomBox = False

# Define the coordinates for the boxes for scoring
# Hoop Box Coordinates
x1=970; y1=870
x2=1070; y2=885
# Bottom Box Coordinates
x3=1000; y3=970
x4=1060 ;y4=985

hoop_box = (x1, y1, x2, y2)  # Coordinates for the hoop box
bottom_box = (x3, y3, x4, y4)  # Coordinates for the bottom box

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

        # Threshold the HSV image to get only orange colors (for the ball)
        mask_orange = cv2.inRange(hsv_frame, lower_orange, upper_orange)

        # Find contours in the mask (for the ball)
        contours_orange, _ = cv2.findContours(mask_orange.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the largest contour, which should be the ball
        if len(contours_orange) > 0:
            largest_contour_orange = max(contours_orange, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour_orange)
            center = (int(x), int(y))

            # Draw a circle around the detected ball
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)

            # Append the center to the ball_positions list
            ball_positions.append(center)

            # Draw a line connecting the ball positions
            for i in range(1, len(ball_positions)):
                cv2.line(frame, ball_positions[i - 1], ball_positions[i], (255, 0, 0), 2)

            # Check if the ball is in the hoop_box or bottom_box
            if hoop_box[0] <= center[0] <= hoop_box[2] and hoop_box[1] <= center[1] <= hoop_box[3]:
                touchHoopBox = True
            elif bottom_box[0] <= center[0] <= bottom_box[2] and bottom_box[1] <= center[1] <= bottom_box[3]:
                touchBottomBox = True

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

if (touchBottomBox and touchBottomBox) == True:
    print("SCHMONEY")
else:
    print("BRICK")

# Release the video capture object
cap.release()

# Closes all the windows currently opened.
cv2.destroyAllWindows()