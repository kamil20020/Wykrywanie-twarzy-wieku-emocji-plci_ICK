import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from AddUser import AddUser
from CalibrateUser import CalibrateUser
from DetectUser import DetectUser
from DetectHistory import DetectHistory
from MainMenu import MainMenu
from FaceRegistration import FaceRegistration
from Help import Help


class FaceRecognitionApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Configure the main window
        tk.Tk.wm_title(self, "Face recognition application")

        # Set background color of the main window
        self.configure(bg="white") 

        # Create a container to hold all the frames
        container = tk.Frame(self, bg="white")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize a dictionary to store frames
        self.frames = {}

        # Create and add frames to the dictionary
        for F in (MainMenu, AddUser, CalibrateUser, DetectUser, DetectHistory, FaceRegistration, Help):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from AddUser import AddUser
from CalibrateUser import CalibrateUser
from DetectUser import DetectUser
from DetectHistory import DetectHistory
from MainMenu import MainMenu
from FaceRegistration import FaceRegistration
from Help import Help


class FaceRecognitionApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Configure the main window
        tk.Tk.wm_title(self, "Face recognition application")

        # Set background color of the main window
        self.configure(bg="white") 

        # Create a container to hold all the frames
        container = tk.Frame(self, bg="white")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize a dictionary to store frames
        self.frames = {}

        # Create and add frames to the dictionary
        for F in (MainMenu, AddUser, CalibrateUser, DetectUser, DetectHistory, FaceRegistration, Help):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.event_generate("<<ShowFrame>>")

        # Show the initial frame
        self.show_frame("MainMenu")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


        # Show the initial frame
        self.show_frame("MainMenu")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
