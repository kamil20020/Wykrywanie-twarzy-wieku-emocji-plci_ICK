import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as fnt
import os
from utilityFunctions import changeOnHover

class Help(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        logoHelpImage = PhotoImage(file="./assets/help64.png")
        backButtonImage = PhotoImage(file="./assets/back64.png")

        camOffIndicator = tk.Label(self, height=2, width=4, bg="red", text="CAM\nOFF", fg="white")
        camOffIndicator.place(x=575, y=25)
        camOnIndicator = tk.Label(self, height=2, width=4, bg="#30572c", text="", fg="white")
        camOnIndicator.place(x=575, y=65)

        labellogoHelp = tk.Label(self, text="Pomoc", image=logoHelpImage, compound = TOP, pady=10, font = fnt.Font(size = 14), bg="white")
        labellogoHelp.image = logoHelpImage

        helpText = Text(self, height = 26, width = 60, bg = "white")
        helpText.insert('1.0', '1. Na początku zarejestruj użytkownika klikając w przycisk \n"Dodaj użytkownika" \n\n2. Po dodaniu użytkownika skalibruj jego twarz klikając w \nprzycisk "Kalibruj użytkownika" \n\n3. Wybierz z rozwijanej listy jakiego użytkownika chcesz \nzarejestrować a następnie wybierz "Kalibruj twarz" \n\n4. Patrz się w kamere aż nie zostanie pobrane X próbek \nTwojej twarzy. \n\n5. Następnie kliknij przycisk "Trenuj model" aby program \npowiązał Twój pseudonim z zeskanowaną twarzą \n\n6. Kliknij "Wykryj użytkownika" z poziomu menu aby przejść \ndo ekranu z podglądem kamery pod którą zostaną wypisane \ninformacje takie jak: pseudonim zeskanowanego użytkownika, \np#d1d1d1ykcja jego płci, wieku oraz emocji')
        helpText.config(state=DISABLED)

        # Button to go back to the main menu
        backButton = tk.Button(self, text="Wstecz", image=backButtonImage, borderwidth=0, compound = TOP, bg="white", cursor="hand2", command=lambda: controller.show_frame("MainMenu"))
        backButton.image = backButtonImage
        changeOnHover(backButton, "#d1d1d1", "white")

        labellogoHelp.pack()
        helpText.pack(pady=20)
        backButton.pack()