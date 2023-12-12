import cv2
import hashlib
import os

# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):
        
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def load_users():
    users = []

    with open('pwd', 'r') as file:

        for line in file:
            username = line.split(":")[0]
            users.append(username)

    return users

def getUsername(given_id):
    with open('pwd', 'r') as file:
        for line in file:
            stored_username, _, id = line.strip().split(':')
            if str(given_id) == id:
                return stored_username
    
    return ""
            
def hash_password(password):
    # Hash the password using a secure hashing algorithm
    # hashlib.sha256 is used in this example
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def append_user(username, password_hash):
    with open('pwd', 'a') as file:
        file.write(f"{username}:{password_hash}:{len(load_users()) + 1}\n")
     
def authenticate_user(username, password_hash):
    with open('pwd', 'r') as file:
        for line in file:
            stored_username, stored_password, id = line.strip().split(':')
            if username == stored_username and password_hash == stored_password:
                return [stored_username, id]
    return None

def compare_passwords(p1, p2):
    return p1 == p2
    
def checkIfInputsEmpty(input):
    return len(input) == 0

def checkIfUserExists(username):
    return username in load_users()

def checkIfUserDirExist(username):
    
    path = "./data/" + username
    
    if os.path.exists(path) and os.path.isdir(path):
        return True
    else:
        return False