import tkinter as tk 
from tkinter import *
import tkinter.font as fnt
from PIL import Image, ImageTk 
import os
import cv2
from utilityFunctions import changeOnHover
from Camera import turnOn, turnOff, getFrame, isOpened
from DetectUser import face_cascade
from CreateClassifier import train_classifer
from tkinter import messagebox

class FaceRegistration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        self.controller = controller
        
        logoRegisterFaceImage = PhotoImage(file="./assets/faceRegister64.png")
        backToCalibrationButtonImage = PhotoImage(file="./assets/back64.png")
        self.cameraOnButtonImage = PhotoImage(file="./assets/cameraOn64.png")
        self.cameraOffPlaceholder500x350Image = PhotoImage(file="./assets/cameraOffPlaceholder500x350.png")

        self.camera_image = tk.Label(self, image=self.cameraOffPlaceholder500x350Image)
        self.num_of_samples = 0
        self.progress = 0
        
        self.labelProgress = tk.Label(self, text="Postęp: 0%", pady=5, font = fnt.Font(size = 14), bg="white")
        
        navButtonsFrame = tk.Frame(self, bg="white", pady=10)
        
        labellogoRegisterFace = tk.Label(self, text="Rejestracja twarzy", image=logoRegisterFaceImage, compound = TOP, pady=10, font = fnt.Font(size = 16), bg="white")
        labellogoRegisterFace.image = logoRegisterFaceImage

        labelRegisterFaceInfo = tk.Label(self, text="Spójrz prosto w kamerę przy optymalnym oświetleniu aby uzyskać jak najlepsze wyniki", bg="white")
        
        backToCalibrationButton = tk.Button(navButtonsFrame, text="Wstecz", image=backToCalibrationButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: [controller.show_frame("CalibrateUser"), self.turnOffCamera(), self.resetProgresAndButton()])
        backToCalibrationButton.image = backToCalibrationButtonImage
        backToCalibrationButton.pack(side='left', padx=50)
        changeOnHover(backToCalibrationButton, "#d1d1d1", "white")
       
        self.registerFaceButton = tk.Button(navButtonsFrame, text="Rejestruj twarz", image=self.cameraOnButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: self.registerFace())
        self.registerFaceButton.image = self.cameraOnButtonImage
        self.registerFaceButton.pack(side='left', padx=50)
        changeOnHover(self.registerFaceButton, "#d1d1d1", "white")

        labellogoRegisterFace.pack()
        labelRegisterFaceInfo.pack()
        self.camera_image.pack(pady=20)
        self.labelProgress.pack()
        navButtonsFrame.pack()

        #self.controller.num_of_images = x
    
    def registerFace(self):
        if self.num_of_samples != 0:
            return

        self.registerFaceButton["state"] = "disabled"
        turnOn()
        self.prepareRegister()
        self.registerSamples()
         
    def turnOffCamera(self):
        self.camera_image.configure(image=self.cameraOffPlaceholder500x350Image)
        turnOff()
        
    def prepareRegister(self):
        try:
            os.makedirs("./data/" + self.controller.loggedUser)
        except:
            print('Directory Already Created')

    def resetProgresAndButton(self):
        self.labelProgress.configure(text="Progres: 0%")
        self.registerFaceButton["state"] = "normal"
        self.num_of_samples = 0
    
    def registerSamples(self):
        frame = getFrame()

        if frame is None or not isOpened():
            return
        
        if self.num_of_samples == 300:
            self.turnOffCamera()
            self.num_of_samples = 0
            self.registerFaceButton["state"] = "normal"
            return

        # Convert into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        face = None

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w].copy()
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        try :
            self.num_of_samples += 1
            cv2.imwrite("./data/" + self.controller.loggedUser + "/" + str(self.num_of_samples) + self.controller.loggedUser + ".jpg", face)
            
            percentage = round(self.num_of_samples / 300 * 100)
            self.labelProgress.configure(text="Progres: " + str(percentage) + "%")
        except :
            print("Could not create img")

        
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
        self.camera_image.after(10, self.registerSamples)
