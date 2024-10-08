#this code allows for the window to stay open and open no matter what

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def rescale(frame,rezhor=int(input("Introdu rezolutia orizontala: ")),rezvert=int(input("Introdu rezolutia verticala: "))):
    dimens=(rezhor,rezvert)
    return cv2.resize(frame,dimens)

camera=cv2.VideoCapture(0)

if not camera.isOpened():
    print("Eroare la camera")
    exit()

while camera.isOpened():
    isTrue, frame=camera.read() 

    if not isTrue:
        print("Frameul nu a putut fi citit")
        exit()

    framechanged=rescale(frame)

    bbox, label, conf = cv.detect_common_objects(framechanged, model="yolov3-tiny")

    for i in conf:
        if i>=0:
            output_image = draw_bbox(framechanged, bbox, label, conf)
            cv2.imshow("Fereastra Principala", output_image)
        else:
            pass

    cv2.imshow("Fereastra Principala",framechanged)

    if cv2.waitKey(1) & 0xFF==ord("c"):
        break


camera.release()
cv2.destroyAllWindows()