import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
import os
from utilityFunctions import changeOnHover


class DetectHistory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")

        def togglePasswordVisibility():
            if entryPassword['show'] == '*':
                entryPassword.config(show='')
                showHidePasswordButton.configure(image=hidePasswordImage)
            else:
                entryPassword.config(show='*')
                showHidePasswordButton.configure(image=showPasswordImage)
        
        logoHistoryImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "history64.png"))
        showPasswordImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "show24.png"))
        hidePasswordImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "hide24.png"))
        backButtonImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "back64.png"))
        confirmButtonImage = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "confirm64.png"))

        labellogoHistory = tk.Label(self, text="Historia wykrywania", image=logoHistoryImage, compound = TOP, pady=20, font = fnt.Font(size = 12), bg="white")
        labellogoHistory.image = logoHistoryImage

        labelChooseUsername = tk.Label(self, text="Wybierz użytkownika: ", bg="white")
        #Dropdown to choose user
        users = ['Andrzej', 'Krzysztof', 'Paweł', 'Maciej']
        variable = StringVar()
        variable.set("Wybierz użytkownika")
        chooseUserDropdown = ttk.OptionMenu(self, variable, *users) 
        #chooseUserDropdown.config(width=30)

        labelTypePassword = tk.Label(self, text="Podaj hasło: ", bg="white")
        entryPassword = ttk.Entry(self, show="*", textvariable="password")
        showHidePasswordButton = tk.Button(self, image=showPasswordImage, bg="white", borderwidth=0, compound = TOP, pady = 10, cursor="hand2", command=togglePasswordVisibility)
        showHidePasswordButton.image = showPasswordImage
        changeOnHover(showHidePasswordButton, "#d1d1d1", "white")

        historyTextPlaceholder = Text(self, height = 20, width = 50, bg = "white")
        historyTextPlaceholder.insert('1.0', '10.11.2023 14:25 Maciej, smutny, mężczyzna, 39 lat18.02.2024 12:05 Tomasz, wesoły, mężczyzna, 21 lat')
        historyTextPlaceholder.config(state=DISABLED)

        # Button to go back to the main menu
        backButton = tk.Button(self, text="Wstecz", image=backButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: controller.show_frame("MainMenu"))
        backButton.image = backButtonImage
        changeOnHover(backButton, "#d1d1d1", "white")

        confirmButton = tk.Button(self, text="Potwierdź", image=confirmButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2")
        confirmButton.image = confirmButtonImage
        changeOnHover(confirmButton, "#d1d1d1", "white")

        labellogoHistory.pack()
        labelChooseUsername.pack()
        chooseUserDropdown.pack()
        labelTypePassword.pack()
        entryPassword.pack()
        showHidePasswordButton.pack()
        historyTextPlaceholder.pack()
        backButton.pack(side='left')
        confirmButton.pack()