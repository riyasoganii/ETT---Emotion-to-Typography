from keras.models import model_from_json
import numpy as np
import cv2
import argparse
import os
# import dependencies
from IPython.display import display, Javascript, Image
from base64 import b64decode, b64encode
from cv2 import *
import numpy as np
import PIL
import io
import html
import time


camera_port = 0 
ramp_frames = 30 
camera = cv2.VideoCapture(camera_port)

def get_image():
    for i in range(ramp_frames):
        temp = camera.read()
    retval, im = camera.read()
    return im 

class FacialExpressionModel(object):
    EMOTIONS_LIST = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

    def __init__(self, model_json_file, model_weights_file):
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        self.loaded_model.load_weights(model_weights_file)
        #print("Model loaded from disk")
        #self.loaded_model.summary()

    def predict_emotion(self, img):
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
cap.set(cv2.CAP_PROP_FPS, (30))

def start_app(cnn):
    img = cv2.imread('photo.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
            fc = gray[y:y + h, x:x + w]
            roi = cv2.resize(fc, (48, 48))
            pred = cnn.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
            if pred == None:
                pred="Neutral"
            print("Predicted emotion: "+ str(pred))
            file = open("emotions.txt","a")
            file.write(str(pred)+" ")
            file.close()

print("Type a sentence! ")
file = open("emotions.txt","w")
file.close()
file=open("text.txt","w")
file.close()

def run():
    text=input()
    file = open("text.txt","a")
    file.write(str(text)+" ")
    file.close()
    camera_capture = get_image()
    cv2.imshow("photo", camera_capture)
    cv2.imwrite("photo.jpg",camera_capture)
    cv2.waitKey(0)
    cv2.destroyWindow("photo")
    model = FacialExpressionModel("model.json", "weights.h5")
    start_app(model)
    if text.find(".")==-1:
        run()
    else:
        return
    
run()
