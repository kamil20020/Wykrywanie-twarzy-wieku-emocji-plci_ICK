import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
import os
import utilityFunctions as uf
from CreateClassifier import train_classifer

class CalibrateUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")

        self.controller = controller
        
        def togglePasswordVisibility():
            if self.passwordEntry['show'] == '*':
                self.passwordEntry.config(show='')
                showHidePasswordButton.configure(image=hidePasswordImage)
            else:
                self.passwordEntry.config(show='*')
                showHidePasswordButton.configure(image=showPasswordImage)

        logoCalibrateImage = PhotoImage(file="./assets/calibrate128.png")
        showPasswordImage = PhotoImage(file="./assets/show24.png")
        hidePasswordImage = PhotoImage(file="./assets/hide24.png")
        registerFaceImage = PhotoImage(file="./assets/faceRegister64.png")
        trainModelImage = PhotoImage(file="./assets/train64.png")
        backButtonImage = PhotoImage(file="./assets/back64.png")

        camOffIndicator = tk.Label(self, height=2, width=4, bg="red", text="CAM\nOFF", fg="white")
        camOffIndicator.place(x=575, y=25)
        camOnIndicator = tk.Label(self, height=2, width=4, bg="#30572c", text="", fg="white")
        camOnIndicator.place(x=575, y=65)

        labellogoCalibrateUser = tk.Label(self, text="Kalibracja użytkownika", image=logoCalibrateImage, compound = TOP, pady=20, font = fnt.Font(size = 18), bg="white")
        labellogoCalibrateUser.image = logoCalibrateImage

        #Label for info if user has been sucessfully registe#d1d1d1 or not
        self.labelRegistrationInfo = tk.Label(self, text="", bg="white", pady=5)

        registerInfoFrame = tk.Frame(self, bg="white", pady=5)
        registerInputsFrame = tk.Frame(registerInfoFrame, bg="white", pady=5)
        registerInputsFrame.pack(side='left')

        #Username entry
        usernameFrame = tk.Frame(registerInputsFrame, bg="white", pady=5)
        usernameFrame.pack(anchor=tk.E)
        labelUsername = tk.Label(usernameFrame, text="Podaj nazwę: ", bg="white").pack(side='left', padx=5)
        self.usernameEntry = ttk.Entry(usernameFrame, textvariable="username")
        self.usernameEntry.pack(side='right')

        #Password entry
        passwordFrame = tk.Frame(registerInputsFrame, bg="white", pady=5)
        passwordFrame.pack(anchor=tk.E)
        labelPassword = tk.Label(passwordFrame, text="Podaj hasło: ", bg="white").pack(side='left', padx=5)
        self.passwordEntry = ttk.Entry(passwordFrame, show="*", textvariable="password")
        self.passwordEntry.pack(side='left')

        #Button to show and hide password
        showHidePasswordButton = tk.Button(registerInfoFrame, image=showPasswordImage, bg="white", borderwidth=0, compound = TOP, pady = 10, cursor="hand2", command=togglePasswordVisibility)
        showHidePasswordButton.image = showPasswordImage
        showHidePasswordButton.pack(side='left', padx=5, pady=7, anchor=tk.S)
        uf.changeOnHover(showHidePasswordButton, "#d1d1d1", "white")

        utilButtonsFrame = tk.Frame(self, bg="white")

        # Button to go FaceRegistration frame
        faceRegistrationButton = tk.Button(utilButtonsFrame, text="Rejestruj twarz", image=registerFaceImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: self.moveToFaceRegisteration())
        faceRegistrationButton.image = registerFaceImage
        faceRegistrationButton.pack(side='left', padx=45)
        uf.changeOnHover(faceRegistrationButton, "#d1d1d1", "white")

        # Button to train model
        trainModelButton = tk.Button(utilButtonsFrame, text="Trenuj model", image=trainModelImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: self.trainModel())
        trainModelButton.image = trainModelImage
        trainModelButton.pack(side='left', padx=45)
        uf.changeOnHover(trainModelButton, "#d1d1d1", "white")

        
        # Button to go back to the main menu
        backButton = tk.Button(self, text="Wstecz", image=backButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: [controller.show_frame("MainMenu"), self.clearInputs()])
        backButton.image = backButtonImage
        uf.changeOnHover(backButton, "#d1d1d1", "white")

        
        labellogoCalibrateUser.pack()
        self.labelRegistrationInfo.pack(pady=10)
        registerInfoFrame.pack(pady=15)
        utilButtonsFrame.pack(pady=30)
        backButton.pack(pady=30)

    def authenticate(self):
        username = self.usernameEntry.get()
        password_hash = uf.hash_password(self.passwordEntry.get())

        if uf.checkIfInputsEmpty(username) or uf.checkIfInputsEmpty(self.passwordEntry.get()):
            self.labelRegistrationInfo.config(text="Proszę wypełnić wszystkie pola", fg="red")
            return False
        
        if not uf.authenticate_user(username, password_hash):
            self.labelRegistrationInfo.config(text="Podano nieprawidłowe dane", fg="red")
            return False
        
        return True
        
    def moveToFaceRegisteration(self):

        if self.authenticate():
            self.controller.loggedUser = self.usernameEntry.get()
            self.controller.show_frame("FaceRegistration")
        
    def trainModel(self):

        if self.authenticate():

            loggedUser = self.usernameEntry.get()
            
            if not uf.checkIfUserDirExist(loggedUser):
                self.labelRegistrationInfo.config(text="Przed trenowaniem modelu należy zarejestrować twarz", fg="red")
            else:
                train_classifer(loggedUser)
                self.labelRegistrationInfo.config(text="Wytrenowano model", fg="green")
                
    def clearInputs(self):
        self.usernameEntry.delete(0, tk.END)
        self.passwordEntry.delete(0, tk.END)
        self.labelRegistrationInfo.config(text="")