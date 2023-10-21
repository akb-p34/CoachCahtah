import cv2

# Load a pre-trained cascade classifier for detecting a person
person_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Load the video
cap = cv2.VideoCapture('IMG_2659.mp4')

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for object detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect people in the frame
    people = person_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in people:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Check if the person is in a shooting position
        if y < frame.shape[0] // 2:
            feedback = "Your shooting formation looks good."
        else:
            feedback = "Adjust your position for a better shot."

        cv2.putText(frame, feedback, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame with feedback
    cv2.imshow('Basketball Coaching App', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()



