import cv2
#from mtcnn.mtcnn import MTCNN
from keras.models import load_model
from keras_preprocessing.image import img_to_array
import numpy as np

#detector= MTCNN()

emotion_model = "./data/_mini_XCEPTION.106-0.65.hdf5"
ageProto="./data/age_deploy.prototxt"
ageModel="./data/age_net.caffemodel"
genderProto="./data/gender_deploy.prototxt"
genderModel="./data/gender_net.caffemodel"

#MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList=['mezczyzna','kobieta']
Emotions = ["zly","zniesmaczony","przestraszony","szczesliwy","smutny","zaskoczony","neutralny"]

emotion_classifier = load_model(emotion_model,compile=False)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

def age(face):
    #Moze zmiana na rozmiar (48, 48) pomoze
    blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), swapRB=True)
    ageNet.setInput(blob)
    agePreds = ageNet.forward()
    print(ageList[agePreds[0].argmax()])

    return ageList[agePreds[0].argmax()]

def gender(face):
    #Moze zmiana na rozmiar (48, 48) pomoze
    blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), swapRB=True)
    genderNet.setInput(blob)
    genderPreds = genderNet.forward()
    print(genderList[genderPreds[0].argmax()])
    
    return genderList[genderPreds[0].argmax()]

def emotion(face):
    face = cv2.resize(face, (48, 48))
    face = face.astype("float") / 255.0
    face = img_to_array(face)
    face = np.expand_dims(face, axis=0)
    preds = emotion_classifier.predict(face)[0]
    emotion_probability = np.max(preds)
    label = Emotions[preds.argmax()]

    print(emotion_probability, label)

    return label