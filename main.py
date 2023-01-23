import cv2
import numpy as np
import dlib 
from imutils import face_utils

cap=cv2.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
sleep=0
drowsy=0
active=0
status=""
color=(0,0,0)
