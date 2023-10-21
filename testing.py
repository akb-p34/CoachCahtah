import cv2

cap = cv2.VideoCapture('IMG_2659.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        cv2.imshow('frame', frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()