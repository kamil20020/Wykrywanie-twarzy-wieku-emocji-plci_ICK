import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
import os
from utilityFunctions import changeOnHover

class CalibrateUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        def togglePasswordVisibility():
            if entryPassword['show'] == '*':
                entryPassword.config(show='')
                showHidePasswordButton.configure(image=hidePasswordImage)
            else:
                entryPassword.config(show='*')
                showHidePasswordButton.configure(image=showPasswordImage)

        logoCalibrateImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "calibrate128.png"))
        showPasswordImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "show24.png"))
        hidePasswordImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "hide24.png"))
        registerFaceImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "faceRegister64.png"))
        trainModelImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "train64.png"))
        backButtonImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "back64.png"))


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
        faceRegistrationButton = tk.Button(utilButtonsFrame, text="Rejestruj twarz", image=registerFaceImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: controller.show_frame("FaceRegistration"))
        faceRegistrationButton.image = registerFaceImage
        faceRegistrationButton.pack(side='left', padx=45)
        changeOnHover(faceRegistrationButton, "#d1d1d1", "white")

        # Button to train model
        trainModelButton = tk.Button(utilButtonsFrame, text="Trenuj model", image=trainModelImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2")
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