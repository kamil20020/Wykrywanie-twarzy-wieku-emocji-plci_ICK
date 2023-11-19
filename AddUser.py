import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
import os
from utilityFunctions import changeOnHover

class AddUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        def togglePasswordVisibility():
            if passwordEntry['show'] == '*':
                passwordEntry.config(show='')
                passwordAgainEntry.config(show='')
                showHidePasswordButton.configure(image=hidePasswordImage)
            else:
                passwordEntry.config(show='*')
                passwordAgainEntry.config(show='*')
                showHidePasswordButton.configure(image=showPasswordImage)


        logoAddUserImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "add-user128.png"))
        backButtonImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "back64.png"))
        confirmButtonImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "confirm64.png"))
        showPasswordImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "show24.png"))
        hidePasswordImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "hide24.png"))

        #Logo for adding new user screen
        labellogoAddUser = tk.Label(self, text="Dodawanie użytkownika", image=logoAddUserImage, compound = TOP, pady=20, font = fnt.Font(size = 18), bg="white")
        labellogoAddUser.image = logoAddUserImage

        #Label for info if user has been sucessfully registe#d1d1d1 or not
        labelRegistrationInfo = tk.Label(self, text="Pomyślnie dodano użytkownika", fg='green', bg="white", pady=25)

        #Username entry
        usernameFrame = tk.Frame(self, bg="white", pady=5)
        labelUsername = tk.Label(usernameFrame, text="Podaj nazwę: ", bg="white").pack(side='left', padx=5)
        usernameEntry = ttk.Entry(usernameFrame, textvariable="username").pack(side='right')


        #Password entry
        passwordFrame = tk.Frame(self, bg="white", pady=5)
        labelPassword = tk.Label(passwordFrame, text="Podaj hasło: ", bg="white").pack(side='left', padx=5)
        passwordEntry = ttk.Entry(passwordFrame, show="*", textvariable="password")
        passwordEntry.pack(side='left')

        #Button to show and hide password
        showHidePasswordButton = tk.Button(passwordFrame, image=showPasswordImage, bg="white", borderwidth=0, compound = TOP, pady = 10, cursor="hand2", command=togglePasswordVisibility)
        showHidePasswordButton.image = showPasswordImage
        showHidePasswordButton.pack(side='left', padx=5)
        changeOnHover(showHidePasswordButton, "#d1d1d1", "white")

        #Password again entry
        passwordAgainFrame = tk.Frame(self, bg="white", pady=5)
        labelPasswordAgain = tk.Label(passwordAgainFrame, text="Podaj hasło ponownie: ", bg="white").pack(side='left', padx=5)
        passwordAgainEntry = ttk.Entry(passwordAgainFrame, show="*", textvariable="passwordAgain")
        passwordAgainEntry.pack(side='right')
    
        #Frame for back and confirm buttons
        navButtonsFrame = tk.Frame(self, bg="white", pady=100)

        # Button to go back to the main menu
        backButton = tk.Button(navButtonsFrame, text="Wstecz", image=backButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: controller.show_frame("MainMenu"))
        backButton.image = backButtonImage
        backButton.pack(side='left', padx=50)
        changeOnHover(backButton, "#d1d1d1", "white")

        # Button to confirm registration
        confirmButton = tk.Button(navButtonsFrame, text="Potwierdź", image=confirmButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2")
        confirmButton.image = confirmButtonImage
        confirmButton.pack(side='left', padx=50)
        changeOnHover(confirmButton, "#d1d1d1", "white")



        labellogoAddUser.pack()
        labelRegistrationInfo.pack()
        usernameFrame.pack()
        passwordFrame.pack()
        passwordAgainFrame.pack()
        navButtonsFrame.pack()