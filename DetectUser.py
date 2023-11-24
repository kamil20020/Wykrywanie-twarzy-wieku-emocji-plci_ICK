import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
from PIL import Image, ImageTk 
import cv2
import os
from utilityFunctions import changeOnHover
from Camera import turnOff, getFrame, turnOn, isOpened

# Load the cascade
face_cascade = cv2.CascadeClassifier('./assets/haarcascade_frontalface_default.xml')

class DetectUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        backButtonImage = PhotoImage(file="./assets/back64.png")
        logoDetectUserImage = PhotoImage(file="./assets/webcam64.png")
        self.cameraOnButtonImage = PhotoImage(file="./assets/cameraOn64.png")
        self.cameraOffButtonImage = PhotoImage(file="./assets/cameraOff64.png")
        self.cameraOffPlaceholder500x350Image = PhotoImage(file="./assets/cameraOffPlaceholder500x350.png")

        labellogoDetectUser = tk.Label(self, text="Wykrywanie użytkownika", image=logoDetectUserImage, compound = TOP, pady=10, font = fnt.Font(size = 10), bg="white")
        labellogoDetectUser.image = logoDetectUserImage

        self.camera_image = tk.Label(self, image=self.cameraOffPlaceholder500x350Image)

        labelUserDetected = tk.Label(self, text="Pseudonim: ", bg="white")
        labelGenderDetected = tk.Label(self, text="Płeć: ", bg="white")
        labelAgeDetected = tk.Label(self, text="Wiek: ", bg="white")
        labelEmotionsDetected = tk.Label(self, text="Emocje: ", bg="white")

        navButtonsFrame = tk.Frame(self, bg="white", pady=10)
        
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
        labelUserDetected.pack()
        labelGenderDetected.pack()
        labelAgeDetected.pack()
        labelEmotionsDetected.pack()
        navButtonsFrame.pack()

    def turnOffCamera(self):
        self.toggleCameraButton.configure(image=self.cameraOnButtonImage, text="Włącz kamerę")
        self.camera_image.configure(image=self.cameraOffPlaceholder500x350Image)
        turnOff()
        
    def toggleCamera(self):

        if not isOpened():
           self.toggleCameraButton.configure(image=self.cameraOffButtonImage, text="Wyłącz kamerę")
           self.setupCameraForDetection()
           
        else:
           self.toggleCameraButton.configure(image=self.cameraOnButtonImage, text="Włącz kamerę")
           self.camera_image.configure(image=self.cameraOffPlaceholder500x350Image)
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

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

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