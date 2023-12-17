import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
import os
from utilityFunctions import changeOnHover
import utilityFunctions as uf


class DetectHistory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")

        def togglePasswordVisibility():
            if self.passwordEntry['show'] == '*':
                self.passwordEntry.config(show='')
                self.showHidePasswordButton.configure(image=hidePasswordImage)
            else:
                self.passwordEntry.config(show='*')
                self.showHidePasswordButton.configure(image=self.showPasswordImage)
        
        logoHistoryImage = PhotoImage(file="./assets/history64.png")
        self.showPasswordImage = PhotoImage(file="./assets/show24.png")
        hidePasswordImage = PhotoImage(file="./assets/hide24.png")
        backButtonImage = PhotoImage(file="./assets/back64.png")
        confirmButtonImage = PhotoImage(file="./assets/confirm64.png")

        camOffIndicator = tk.Label(self, height=2, width=4, bg="red", text="CAM\nOFF", fg="white")
        camOffIndicator.place(x=575, y=25)
        camOnIndicator = tk.Label(self, height=2, width=4, bg="#30572c", text="", fg="white")
        camOnIndicator.place(x=575, y=65)

        labellogoHistory = tk.Label(self, text="Historia wykrywania", image=logoHistoryImage, compound = TOP, pady=10, font = fnt.Font(size = 14), bg="white")
        labellogoHistory.image = logoHistoryImage

        #Label for info if user has been sucessfully registe#d1d1d1 or not
        self.labelRegistrationInfo = tk.Label(self, text="", bg="white")

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
        self.showHidePasswordButton.pack(side='left', padx=5, pady=7, anchor=tk.S)
        changeOnHover(self.showHidePasswordButton, "#d1d1d1", "white")



        textPlaceholderBox = tk.Frame(self, bg="white")

        self.historyTextPlaceholder = Text(textPlaceholderBox, height = 20, width = 65, bg = "white", wrap="none")
        self.historyTextPlaceholder.pack(side='left')
        
        scrollbar = tk.Scrollbar(textPlaceholderBox, orient='vertical', command=self.historyTextPlaceholder.yview)
        scrollbar.pack(side='left', fill=tk.Y)
        self.historyTextPlaceholder['yscrollcommand'] = scrollbar.set


        navButtonsFrame = tk.Frame(self, bg="white")

        # Button to go back to the main menu
        backButton = tk.Button(navButtonsFrame, text="Wstecz", image=backButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: [controller.show_frame("MainMenu"), self.clearInputs()])
        backButton.image = backButtonImage
        changeOnHover(backButton, "#d1d1d1", "white")
        backButton.pack(side='left', padx=50)
        
        confirmButton = tk.Button(navButtonsFrame, text="Potwierdź", image=confirmButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: self.authAndShowHistory())
        confirmButton.image = confirmButtonImage
        changeOnHover(confirmButton, "#d1d1d1", "white")
        confirmButton.pack(side='left', padx=50)

        labellogoHistory.pack()
        self.labelRegistrationInfo.pack()
        self.showHidePasswordButton.pack()
        registerInfoFrame.pack()
        textPlaceholderBox.pack(pady=10)
        navButtonsFrame.pack()
        
        
      
    
    def authAndShowHistory(self):
        if self.authenticate():
            self.showHistory()
            self.labelRegistrationInfo.config(text="Historia wykrywania została wyświetlona", fg="green")
        
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
    
    def showHistory(self):
        self.historyTextPlaceholder.delete('1.0', END)
        currentUser = self.usernameEntry.get()  
        foundResults = []

        with open('history', 'r') as file:
            for line in file:
                if currentUser in line:
                    foundResults.append(line.strip())

        if foundResults:
            for found_line in foundResults:
                self.historyTextPlaceholder.insert('1.0', f"{found_line}\n") 
        else:
            self.historyTextPlaceholder.insert('1.0', 'Brak historii wykrywania dla tego użytkownika!')  
        #self.historyTextPlaceholder.config(state=DISABLED) #ODKOMENTOWAC
    
    def clearInputs(self):
        self.usernameEntry.delete(0, tk.END)
        self.passwordEntry.delete(0, tk.END)
        self.labelRegistrationInfo.config(text="")
        self.historyTextPlaceholder.delete('1.0', END)
        self.passwordEntry.config(show='*')
        self.showHidePasswordButton.configure(image=self.showPasswordImage)