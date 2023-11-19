import cv2

# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):
        
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))