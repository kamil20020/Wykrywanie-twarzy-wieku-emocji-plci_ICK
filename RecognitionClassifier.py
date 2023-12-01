import numpy as np
from PIL import Image
import os, cv2
from utilityFunctions import load_users

clf = cv2.face.LBPHFaceRecognizer_create()

if os.path.exists("./data/recognition-classifier.xml"):
    clf.read("./data/recognition-classifier.xml")

# Method to train custom classifier to recognize face
def train_classifer():

    # Read all the images in custom data-set
    path = os.path.join(os.getcwd() + "/data")

    faces = []
    pictures = []
    labels = []
    users_dirs = []

    for root, dirs, files in os.walk(path):
        users_dirs = dirs
        break

    for i in range(len(users_dirs)):

        user = users_dirs[i]

        user_dir_path = os.path.join(path, user)

        pictures = []

        for _, _, files in os.walk(user_dir_path):
            pictures = files

        for pic in pictures:
            imgpath = os.path.join(user_dir_path, pic)
            img = Image.open(imgpath).convert('L')
            imageNp = np.array(img, 'uint8')
            faces.append(imageNp)
            labels.append(i)


    labelsNp = np.array(labels)

    #Train and save classifier
    clf.train(faces, labelsNp)
    clf.write("./data/recognition-classifier.xml")
    