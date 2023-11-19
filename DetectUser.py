import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
from PIL import Image, ImageTk 
import cv2
import os
from utilityFunctions import changeOnHover
from Camera import turnOff, getFrame, turnOn

class DetectUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        backButtonImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "back64.png"))
        logoDetectUserImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "webcam64.png"))

        labellogoDetectUser = tk.Label(self, text="Wykrywanie użytkownika", image=logoDetectUserImage, compound = TOP, pady=10, font = fnt.Font(size = 10), bg="white")
        labellogoDetectUser.image = logoDetectUserImage

        #detectUserPlaceholder = Text(self, height = 20, width = 50, bg = "white", state=DISABLED)

        self.camera_image = tk.Label(self, height=350, width=500)
        #self.camera_image.bind("Visibility", func=lambda e: self.setupCamera())
        self.bind('<Enter>', self.setupCamera())

        labelUserDetected = tk.Label(self, text="Pseudonim: ", bg="white")
        labelGenderDetected = tk.Label(self, text="Płeć: ", bg="white")
        labelAgeDetected = tk.Label(self, text="Wiek: ", bg="white")
        labelEmotionsDetected = tk.Label(self, text="Emocje: ", bg="white")

        # Button to go back to the main menu
        backButton = tk.Button(self, text="Wstecz", image=backButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: [controller.show_frame("MainMenu"), turnOff()])
        backButton.image = backButtonImage
        changeOnHover(backButton, "#d1d1d1", "white")

        labellogoDetectUser.pack()
        #detectUserPlaceholder.pack()
        self.camera_image.pack()
        labelUserDetected.pack()
        labelGenderDetected.pack()
        labelAgeDetected.pack()
        labelEmotionsDetected.pack()
        backButton.pack()

    def setupCamera(self):
        turnOn()
        self.detectUser()

    def detectUser(self):

        frame = getFrame()

        if frame is None:
            return

        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

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
    
        # Repeat the same process after every 10 seconds 
        self.camera_image.after(20, self.detectUser)
