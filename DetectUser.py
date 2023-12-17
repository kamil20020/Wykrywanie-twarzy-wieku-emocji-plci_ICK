import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
from PIL import Image, ImageTk 
import cv2
import os
from utilityFunctions import changeOnHover, load_users, getUsername, writeToHistory
from Camera import turnOff, getFrame, turnOn, isOpened
from RecognitionClassifier import clf as recognition_classifier
import predictions


#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #ignore error
# Load the cascade
face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')

#Import labela emocji z klasy predictions (nie testowane)

all_users = load_users()

class DetectUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        backButtonImage = PhotoImage(file="./assets/back64.png")
        logoDetectUserImage = PhotoImage(file="./assets/webcam64.png")
        self.cameraOnButtonImage = PhotoImage(file="./assets/cameraOn64.png")
        self.cameraOffButtonImage = PhotoImage(file="./assets/cameraOff64.png")
        self.cameraOffPlaceholder500x350Image = PhotoImage(file="./assets/cameraOffPlaceholder500x350.png")

        self.camOffIndicator = tk.Label(self, height=2, width=4, bg="red", text="CAM\nOFF", fg="white")
        self.camOffIndicator.place(x=575, y=25)
        self.camOnIndicator = tk.Label(self, height=2, width=4, bg="#30572c", text="", fg="white")
        self.camOnIndicator.place(x=575, y=65)

        labellogoDetectUser = tk.Label(self, text="Wykrywanie użytkownika", image=logoDetectUserImage, compound = TOP, pady=10, font = fnt.Font(size = 10), bg="white")
        labellogoDetectUser.image = logoDetectUserImage

        self.camera_image = tk.Label(self, image=self.cameraOffPlaceholder500x350Image)

        # labelsFrame = tk.Frame(self, bg="white")
        # self.labelUserDetected = tk.Label(labelsFrame, text="Pseudonim: nie wykryto", bg="white", fg="red").pack(anchor=tk.W)
        # self.labelGenderDetected = tk.Label(labelsFrame, text="Płeć: nie wykryto", bg="white", fg="red").pack(anchor=tk.W)
        # self.labelAgeDetected = tk.Label(labelsFrame, text="Wiek: nie wykryto", bg="white", fg="red").pack(anchor=tk.W)
        # self.labelEmotionsDetected = tk.Label(labelsFrame, text="Emocje: nie wykryto", bg="white", fg="red").pack(anchor=tk.W)

        navButtonsFrame = tk.Frame(self, bg="white")
        
        # Button to go back to the main menu
        backButton = tk.Button(navButtonsFrame, text="Wstecz", image=backButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: [controller.show_frame("MainMenu"), self.turnOffCamera()])
        backButton.image = backButtonImage
        backButton.pack(side='left', padx=50)
        changeOnHover(backButton, "#d1d1d1", "white")
        
        self.toggleCameraButton = tk.Button(navButtonsFrame, text="Włącz kamerę", image=self.cameraOnButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: self.toggleCamera())
        self.toggleCameraButton.image = self.cameraOnButtonImage
        self.toggleCameraButton.pack(side='left', padx=50)
        changeOnHover(self.toggleCameraButton, "#d1d1d1", "white")

        labellogoDetectUser.pack()
        self.camera_image.pack()
        # labelsFrame.pack(pady=10)
        navButtonsFrame.pack(pady=50)

    def turnOffCamera(self):
        self.toggleCameraButton.configure(image=self.cameraOnButtonImage, text="Włącz kamerę")
        self.camera_image.configure(image=self.cameraOffPlaceholder500x350Image)
        self.camOffIndicator.configure(text="CAM\nOFF", bg="red", fg="white")
        self.camOnIndicator.configure(text="", bg="#30572c")
        turnOff()
        
    def toggleCamera(self):

        if not isOpened():
           self.toggleCameraButton.configure(image=self.cameraOffButtonImage, text="Wyłącz kamerę")
           self.setupCameraForDetection()
           self.camOffIndicator.configure(text="", bg="#5e2727")
           self.camOnIndicator.configure(text="CAM\nON", bg="#39852a", fg="white")
           
        else:
           self.toggleCameraButton.configure(image=self.cameraOnButtonImage, text="Włącz kamerę")
           self.camera_image.configure(image=self.cameraOffPlaceholder500x350Image)
           self.camOffIndicator.configure(text="CAM\nOFF", bg="red", fg="white")
           self.camOnIndicator.configure(text="", bg="#30572c")
           turnOff()


    def setupCameraForDetection(self):
        turnOn()
        self.detectUser()

    def detectUser(self):

        frame = getFrame()

        if frame is None or not isOpened():
            return

        # Convert into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bgr = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 2, 5)
        fontType = cv2.FONT_HERSHEY_SIMPLEX
        fontSize = 0.4
        
        # if len(faces) == 0:
        #     self.labelUserDetected.configure(text="Pseudonim: nie wykryto")
        #     self.labelGenderDetected.configure(text="Płeć: nie wykryto")
        #     self.labelAgeDetected.configure(text="Wiek: nie wykryto")
        #     self.labelEmotionsDetected.configure(text="Emocje: nie wykryto")

        # Draw the rectangle around each face

        for (x, y, w, h) in faces:

            face = gray[y:y+h,x:x+w]
            colored_face = bgr[y:y+h,x:x+w]

            age = predictions.age(colored_face)
            gender = predictions.gender(colored_face)
            emotion = predictions.emotion(face)

            desc = emotion+", "+gender+", "+age #'21 lat, Mezczyzna, Smutny'

            if os.path.exists("./data/recognition-classifier.xml"):

                label, confidence = recognition_classifier.predict(face)
                confidence = 100 - confidence
                user = getUsername(label)

                print(str(user) + " Confidence: " + str(confidence) + " %")

                if confidence > 50:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, user, (x, y-4), fontType, fontSize, (0, 255, 0), 1, cv2.LINE_AA)
                    cv2.putText(frame, desc, (x, y + h + 12), fontType, fontSize, (0, 255, 0), 1, cv2.LINE_AA)
                    writeToHistory(user, emotion, gender, age)
                    
                else:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.putText(frame, "Niezarejestrowany", (x, y-4), fontType, fontSize, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.putText(frame, desc, (x, y + h + 12), fontType, fontSize, (0, 0, 255), 1, cv2.LINE_AA)
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, "Niezarejestrowany", (x, y-4), fontType, fontSize, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(frame, desc, (x, y + h + 12), fontType, fontSize, (0, 0, 255), 1, cv2.LINE_AA)

        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
  
        # Capture the latest frame and transform to image 
        captured_image = Image.fromarray(opencv_image)
    
        # Convert captured image to photoimage 
        photo_image = ImageTk.PhotoImage(image=captured_image) 
    
        # Displaying photoimage in the label 
        self.camera_image.photo_image = photo_image 
    
        # Configure image in the label 
        self.camera_image.configure(image=photo_image)
    
        # Repeat the same process after every X miliseconds
        self.camera_image.after(50, self.detectUser)