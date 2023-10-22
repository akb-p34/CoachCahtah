import cv2
import numpy as np

# read the image
image = cv2.imread("basketball.jpg")

# convert from BGR to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# define the range of orange color in HSV
lower_orange = np.array([20,20,110])
upper_orange = np.array([255,225,255])

# Threshold the HSV image to get only orange colors
mask = cv2.inRange(hsv_image, lower_orange, upper_orange)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
