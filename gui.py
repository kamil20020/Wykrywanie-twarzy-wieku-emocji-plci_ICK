from tkinter import * 
from tkinter.ttk import *
from FaceRecognitionApp import FaceRecognitionApp

# Run the application
if __name__ == "__main__":
    app = FaceRecognitionApp()
    app.geometry("650x680")  # Set the initial size of the window
    app.resizable(False, False)
    app.mainloop()
