import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
import os
from utilityFunctions import changeOnHover, load_users

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        
        logoMainMenuImage = PhotoImage(file="./assets/logo128.png")
        addUserImage = PhotoImage(file="./assets/add-user64.png")
        calibrationImage = PhotoImage(file="./assets/calibrate64.png")
        webcamImage = PhotoImage(file="./assets/webcam64.png")
        historyImage = PhotoImage(file="./assets/history64.png")
        quitImage = PhotoImage(file="./assets/quit64.png")

        camOffIndicator = tk.Label(self, height=2, width=4, text="CAM\nOFF", bg="red", fg="white")
        camOffIndicator.place(x=575, y=25)
        camOnIndicator = tk.Label(self, height=2, width=4, text="", bg="#30572c", fg="white")
        camOnIndicator.place(x=575, y=65)
        
        # Logo in main menu
        labelLogoMainMenu = tk.Label(self, text="Welcome to the Start Page!", image=logoMainMenuImage, bg="white")
        labelLogoMainMenu.image = logoMainMenuImage

        # Button to navigate to AddUser
        button1 = tk.Button(self, text="Dodaj użytkownika", image=addUserImage, borderwidth=0, bg='white', compound = TOP, cursor="hand2", command=lambda: controller.show_frame("AddUser"))
        button1.image = addUserImage
        changeOnHover(button1, "#d1d1d1", "white")

        # Button to navigate to CalibrateUser
        button2 = tk.Button(self, text="Kalibruj użytkownika", image=calibrationImage, borderwidth=0, bg='white', compound = TOP, cursor="hand2", command=lambda: controller.show_frame("CalibrateUser"))
        button2.image = calibrationImage
        changeOnHover(button2, "#d1d1d1", "white")

        # Button to navigate to DetectUser
        button3 = tk.Button(self, text="Wykryj użytkownika", image=webcamImage, borderwidth=0, bg='white', compound = TOP, cursor="hand2", command=lambda: controller.show_frame("DetectUser"))
        button3.image = webcamImage
        changeOnHover(button3, "#d1d1d1", "white")

        # Button to navigate to DetectHistory
        button4 = tk.Button(self, text="Historia wykrywania", image=historyImage, borderwidth=0, bg='white', compound = TOP, cursor="hand2", command=lambda: controller.show_frame("DetectHistory"))
        button4.image = historyImage
        changeOnHover(button4, "#d1d1d1", "white")

        # Button to navigate to Help
        button5 = tk.Button(self, text="Pomoc", font= ('Helvetica 9 underline'), borderwidth=0, pady=5, padx=5, bg='white', compound = TOP, cursor="hand2", command=lambda: controller.show_frame("Help"))
        changeOnHover(button5, "#d1d1d1", "white")

        # Button to exit
        button6 = tk.Button(self, text="Wyjdź", image=quitImage, borderwidth=0, bg='white', compound = TOP, cursor="hand2", command=controller.destroy)
        button6.image = quitImage
        changeOnHover(button6, "#d1d1d1", "white")

        self.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        labelLogoMainMenu.grid(row = 1, column = 3, sticky = 'nsew')
        button1.grid(row = 4, column = 2)
        button2.grid(row = 4, column = 4)
        button3.grid(row = 6, column = 2)
        button4.grid(row = 6, column = 4)
        button5.grid(row = 10, column = 3)
        button6.grid(row = 8, column = 3)


