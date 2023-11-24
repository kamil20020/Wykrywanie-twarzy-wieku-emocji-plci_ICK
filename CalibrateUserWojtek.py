import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
import os
from utilityFunctions import changeOnHover
#Wojtek ~ 3 potrzebne importy
from CreateDataset import start_capture
from CreateClassifier import train_classifer
from tkinter import messagebox

class CalibrateUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
#Wojtek ~ Deklaracja 3 "self" - wykorzystywane w "def" ponizej
        self.numimglabel = tk.Label(self, text="Number of images captured = 0", font='Helvetica 12 bold', fg="#263942")
        self.controller = controller
#Wojtek ~ Aktualnie nazwa uzytkownika jest hard codem
        self.controller.active_name = "Wojtek"
        
        def togglePasswordVisibility():
            if entryPassword['show'] == '*':
                entryPassword.config(show='')
                showHidePasswordButton.configure(image=hidePasswordImage)
            else:
                entryPassword.config(show='*')
                showHidePasswordButton.configure(image=showPasswordImage)

        logoCalibrateImage = PhotoImage(file="./assets/calibrate128.png")
        showPasswordImage = PhotoImage(file="./assets/show24.png")
        hidePasswordImage = PhotoImage(file="./assets/hide24.png")
        registerFaceImage = PhotoImage(file="./assets/faceRegister64.png")
        trainModelImage = PhotoImage(file="./assets/train64.png")
        backButtonImage = PhotoImage(file="./assets/back64.png")


        labellogoAddUser = tk.Label(self, text="Kalibracja użytkownika", image=logoCalibrateImage, compound = TOP, pady=20, font = fnt.Font(size = 18), bg="white")
        labellogoAddUser.image = logoCalibrateImage

        dropDownFrame = tk.Frame(self, bg="white")

        labelChooseUsername = tk.Label(dropDownFrame, text="Wybierz użytkownika: ", bg="white").pack(side='left', padx=5)
        #Dropdown to choose user
        users = ['Andrzej', 'Krzysztof', 'Paweł', 'Maciej']
        variable = StringVar()
        variable.set("Wybierz użytkownika")
        chooseUserDropdown = ttk.OptionMenu(dropDownFrame, variable, *users).pack(side='left', padx=5)
        #chooseUserDropdown.config(width=30)

        passwordFrame = tk.Frame(self, bg="white", pady=10)

        labelTypePassword = tk.Label(passwordFrame, text="Podaj hasło: ", bg="white").pack(side='left', padx=5)
        entryPassword = ttk.Entry(passwordFrame, show="*", textvariable="password")
        entryPassword.pack(side='left', padx=5)
        showHidePasswordButton = tk.Button(passwordFrame, image=showPasswordImage, bg="white", borderwidth=0, compound = TOP, pady = 10, cursor="hand2", command=togglePasswordVisibility)
        showHidePasswordButton.image = showPasswordImage
        showHidePasswordButton.pack(side='left', padx=5)
        changeOnHover(showHidePasswordButton, "#d1d1d1", "white")

        utilButtonsFrame = tk.Frame(self, bg="white")

        # Button to go FaceRegistration frame
#Wojtek ~ W definicji Buttona dodane "command=self.capimg"
        faceRegistrationButton = tk.Button(utilButtonsFrame, text="Rejestruj twarz", image=registerFaceImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=self.capimg)
        faceRegistrationButton.image = registerFaceImage
        faceRegistrationButton.pack(side='left', padx=45)
        changeOnHover(faceRegistrationButton, "#d1d1d1", "white")

        # Button to train model
#Wojtek ~ W definicji Buttona dodane "command=self.trainmodel"
        trainModelButton = tk.Button(utilButtonsFrame, text="Trenuj model", image=trainModelImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=self.trainmodel)
        trainModelButton.image = trainModelImage
        trainModelButton.pack(side='left', padx=45)
        changeOnHover(trainModelButton, "#d1d1d1", "white")

        
        # Button to go back to the main menu
        backButton = tk.Button(self, text="Wstecz", image=backButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: controller.show_frame("MainMenu"))
        backButton.image = backButtonImage
        changeOnHover(backButton, "#d1d1d1", "white")

        
        labellogoAddUser.pack()
        dropDownFrame.pack(pady=(30,30))
        passwordFrame.pack()
        utilButtonsFrame.pack(pady=(130,30))
        backButton.pack()
#Wojtek ~ Dodane def capimg i def trainmodel
    def capimg(self):
        self.numimglabel.config(text=str("Captured Images = 0 "))
        messagebox.showinfo("INSTRUCTIONS", "We will Capture 300 pic of your Face.")
        x = start_capture(self.controller.active_name)
        self.controller.num_of_images = x
        self.numimglabel.config(text=str("Number of images captured = "+str(x)))
    
    def trainmodel(self):
        if self.controller.num_of_images < 300:
            messagebox.showerror("ERROR", "Not enough Data, Capture at least 300 images!")
            return
        train_classifer(self.controller.active_name)
        messagebox.showinfo("SUCCESS", "The model has been successfully trained!")