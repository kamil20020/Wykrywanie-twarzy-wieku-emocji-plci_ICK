import tkinter as tk 
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
import os
from utilityFunctions import changeOnHover

class FaceRegistration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        logoRegisterFaceImage = PhotoImage(file="./assets/faceRegister128.png")
        backToCalibrationButtonImage = PhotoImage(file="./assets/back64.png")

        labellogoRegisterFace = tk.Label(self, text="Rejestracja twarzy", image=logoRegisterFaceImage, compound = TOP, pady=20, font = fnt.Font(size = 18), bg="white")
        labellogoRegisterFace.image = logoRegisterFaceImage

        labelRegisterFaceInfo = tk.Label(self, text="Spójrz prosto w kamerę przy optymalnym oświetleniu aby uzyskać jak najlepsze wyniki", bg="white")

        cameraPlaceholder = Text(self, height = 20, width = 50, bg = "white", state=DISABLED)

        # Button to go back to the main menu
        backToCalibrationButton = tk.Button(self, text="Wstecz", image=backToCalibrationButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: controller.show_frame("CalibrateUser"))
        backToCalibrationButton.image = backToCalibrationButtonImage
        changeOnHover(backToCalibrationButton, "#d1d1d1", "white")

        labellogoRegisterFace.pack()
        labelRegisterFaceInfo.pack()
        cameraPlaceholder.pack()
        backToCalibrationButton.pack()