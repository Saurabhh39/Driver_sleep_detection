import cv2
import numpy as np
import dlib 
from imutils import face_utils
from pygame import mixer

cap=cv2.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
global sleep
global active
global status
global color

def euclideanDistance(a,b):
    return np.linalg.norm(a - b)

def blinked(a,b,c,d,e,f):
    up=euclideanDistance(b,d) + euclideanDistance(c,e)
    down=euclideanDistance(a,f)
    ear=up/(down*2.0)
    if(ear>0.25):
        return 2
    elif(ear<=0.25 and ear>0.21):
        return 1
    else:
        return 0
    
def landmarks_show():
    while True:
        _,face_frame=cap.read()
        gray=cv2.cvtColor(face_frame, cv2.COLOR_BGR2GRAY)
        faces=detector(gray)

        for face in faces:
            x1=face.left()
            y1=face.top()
            x2=face.right()
            y2=face.bottom()
            cv2.rectangle(face_frame,(x1,y1),(x2,y2),(0,255,0),2)
            landmarks=predictor(gray,face)
            landmarks=face_utils.shape_to_np(landmarks)

        for n in range(0,68):
                (x,y)=landmarks[n]
                cv2.circle(face_frame,(x,y),1,(255,255,255),-1)
        cv2.imshow("Sleep Detection",face_frame)
        key=cv2.waitKey(1)
        if key==27:
            break


def sleep_detector():
    mixer.init()
    sound = mixer.Sound('alarm.wav')
    sleep=0
    active=0
    status=""
    color=(0,0,0)
    while True:
        _,frame=cap.read()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=detector(gray)

        for face in faces:
            x1=face.left()
            y1=face.top()
            x2=face.right()
            y2=face.bottom()
            face_frame=frame.copy()
            cv2.rectangle(face_frame,(x1,y1),(x2,y2),(0,255,0),2)

            landmarks=predictor(gray,face)
            landmarks=face_utils.shape_to_np(landmarks)

            left_blink=blinked(landmarks[36],landmarks[37],landmarks[38],landmarks[41],landmarks[40],landmarks[39])
            right_blink=blinked(landmarks[42],landmarks[43],landmarks[44],landmarks[47],landmarks[46],landmarks[45])

            if(left_blink==0 or right_blink==0):
                sleep+=1
                active=0
                if(sleep>15):
                    status="YOU ARE SLEEPING!"
                    color=(0,0,255)
                    try:
                        sound.play()
                    except:
                        pass
            else:
                sleep=0
                active+=1
                if(active>15):
                    status="YOU ARE ACTIVE"
                    color=(0,255,0)
            cv2.putText(frame,status,(100,100),cv2.FONT_HERSHEY_COMPLEX,1.2,color,2)
        cv2.imshow("Face Detection",frame)
        key=cv2.waitKey(1)
        if key==27:
            break