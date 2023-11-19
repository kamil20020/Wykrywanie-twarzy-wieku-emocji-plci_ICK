import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detectFace(img):

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display image
    cv2.imshow('img', img)

def detectFaceOnImg():

    # Read the input image
    img = cv2.imread('face.png')
    detectFace(img)
    cv2.waitKey()

def detectFaceOnCamera():

    # To capture video from webcam. 
    cap = cv2.VideoCapture(0)

    while True:

        _, img = cap.read()

        # By default camera view is reversed
        img = cv2.flip(img, 1)
        detectFace(img)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break

    # Release the VideoCapture object
    cap.release()

detectFaceOnCamera()