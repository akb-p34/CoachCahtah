import cv2
import numpy as np

# Create a VideoCapture object to read the video
cap = cv2.VideoCapture('IMG_3627.mov')

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

        # Bitwise-AND mask and original frame
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # Display the resulting frame
        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Result', res)

        # Define 'q' as the exit button
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object
cap.release()

# Closes all the windows currently opened.
cv2.destroyAllWindows()