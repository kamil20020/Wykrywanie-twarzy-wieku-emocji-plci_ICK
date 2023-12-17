import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
import os
import utilityFunctions as uf

class AddUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        def togglePasswordVisibility():
            if self.passwordEntry['show'] == '*':
                self.passwordEntry.config(show='')
                self.passwordAgainEntry.config(show='')
                self.showHidePasswordButton.configure(image=hidePasswordImage)
            else:
                self.passwordEntry.config(show='*')
                self.passwordAgainEntry.config(show='*')
                self.showHidePasswordButton.configure(image=self.showPasswordImage)


        logoAddUserImage = PhotoImage(file="./assets/add-user128.png")
        backButtonImage = PhotoImage(file="./assets/back64.png")
        confirmButtonImage = PhotoImage(file="./assets/confirm64.png")
        self.showPasswordImage = PhotoImage(file="./assets/show24.png")
        hidePasswordImage = PhotoImage(file="./assets/hide24.png")

        camOffIndicator = tk.Label(self, height=2, width=4, bg="red", text="CAM\nOFF", fg="white")
        camOffIndicator.place(x=575, y=25)
        camOnIndicator = tk.Label(self, height=2, width=4, bg="#30572c", text="", fg="white")
        camOnIndicator.place(x=575, y=65)

        #Logo for adding new user screen
        labellogoAddUser = tk.Label(self, text="Dodawanie użytkownika", image=logoAddUserImage, compound = TOP, pady=20, font = fnt.Font(size = 18), bg="white")
        labellogoAddUser.image = logoAddUserImage

        #Label for info if user has been sucessfully registe#d1d1d1 or not
        self.labelRegistrationInfo = tk.Label(self, bg="white", pady=25)

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
        self.showHidePasswordButton = tk.Button(registerInfoFrame, image=self.showPasswordImage, bg="white", borderwidth=0, compound = TOP, pady = 10, cursor="hand2", command=togglePasswordVisibility)
        self.showHidePasswordButton.image = self.showPasswordImage
        self.showHidePasswordButton.pack(side='left', padx=5)
        uf.changeOnHover(self.showHidePasswordButton, "#d1d1d1", "white")

        #Password again entry
        passwordAgainFrame = tk.Frame(registerInputsFrame, bg="white", pady=5)
        passwordAgainFrame.pack(anchor=tk.E)
        labelPasswordAgain = tk.Label(passwordAgainFrame, text="Podaj hasło ponownie: ", bg="white").pack(side='left', padx=5)
        self.passwordAgainEntry = ttk.Entry(passwordAgainFrame, show="*", textvariable="passwordAgain")
        self.passwordAgainEntry.pack(side='right')
    
        #Frame for back and confirm buttons
        navButtonsFrame = tk.Frame(self, bg="white", pady=100)

        # Button to go back to the main menu
        backButton = tk.Button(navButtonsFrame, text="Wstecz", image=backButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: [controller.show_frame("MainMenu"), self.clearInputs()])
        backButton.image = backButtonImage
        backButton.pack(side='left', padx=50)
        uf.changeOnHover(backButton, "#d1d1d1", "white")

        # Button to confirm registration
        confirmButton = tk.Button(navButtonsFrame, text="Potwierdź", image=confirmButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: self.register_user())
        confirmButton.image = confirmButtonImage
        confirmButton.pack(side='left', padx=50)
        uf.changeOnHover(confirmButton, "#d1d1d1", "white")

        labellogoAddUser.pack()
        self.labelRegistrationInfo.pack()
        registerInfoFrame.pack()
        navButtonsFrame.pack()

    def register_user(self):
        username = self.usernameEntry.get()
        password_hash = uf.hash_password(self.passwordEntry.get())
        passwordAgain_hash = uf.hash_password(self.passwordAgainEntry.get())

        if uf.checkIfUserExists(username):
            self.labelRegistrationInfo.config(text="Użytkownik o podanej nazwie już istnieje", fg="red")
            return

        if uf.checkIfInputsEmpty(username) or uf.checkIfInputsEmpty(self.passwordEntry.get()) or uf.checkIfInputsEmpty(self.passwordAgainEntry.get()):
            self.labelRegistrationInfo.config(text="Proszę wypełnić wszystkie pola", fg="red")
            return
        
        if not uf.compare_passwords(password_hash, passwordAgain_hash):
            self.labelRegistrationInfo.config(text="Podane hasła nie zgadzają się", fg="red")
            return
        
        self.labelRegistrationInfo.config(text="Pomyślnie zarejestrowano użytkownika", fg="green")
        uf.append_user(username, password_hash)
        self.usernameEntry.delete(0, tk.END)
        self.passwordEntry.delete(0, tk.END)
        self.passwordAgainEntry.delete(0, tk.END)

    def clearInputs(self):
        self.usernameEntry.delete(0, tk.END)
        self.passwordEntry.delete(0, tk.END)
        self.passwordAgainEntry.delete(0, tk.END)
        self.labelRegistrationInfo.config(text="")
        self.passwordEntry.config(show='*')
        self.passwordAgainEntry.config(show='*')
        self.showHidePasswordButton.configure(image=self.showPasswordImage)
        



