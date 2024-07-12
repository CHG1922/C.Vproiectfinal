#the way the code is structured right now does not allow the creation of a window,until an object,which cvlib is certain at least 40% is something from the 80 objects it can recognize,exists,and the window freezes if there is nothing it can recognize/that has an index bigger than 0.4 (even people)

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def rescale(frame,rezhor=int(input("Introdu rezolutia orizontala: ")),rezvert=int(input("Introdu rezolutia verticala: "))):
    indexhor=float(rezhor/640)
    indexver=float(rezvert/480)
    width=int(frame.shape[1]*indexhor)
    height=int(frame.shape[0]*indexver)
    dimens=(width,height)
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
        if i>=0.4:
            output_image = draw_bbox(framechanged, bbox, label, conf)
            cv2.imshow("Fereastra Principala", output_image)
        else:
            pass


    if cv2.waitKey(1) & 0xFF==ord("c"):
        break


camera.release()
cv2.destroyAllWindows()