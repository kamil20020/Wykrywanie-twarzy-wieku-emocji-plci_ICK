import cv2

vid = None

def turnOn():
    global vid

    if vid is not None:
   
        if vid.isOpened():
            return False
        
        vid.retrieve()
        return True

    vid = cv2.VideoCapture(0)
    
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 50) 
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 20)

    return True

def turnOff():
    global vid

    if (vid is None) or (not vid.isOpened()):
        return False

    vid.release()
    vid.retrieve()

    return True

def getFrame():
    global vid

    if vid is None:
        return None

    _, frame = vid.read()

    # By default camera view is reversed
    frame = cv2.flip(frame, 1)

    return frame