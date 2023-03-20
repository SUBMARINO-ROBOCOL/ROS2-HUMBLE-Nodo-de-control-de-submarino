import cv2
from PIL import Image
import numpy as np



cap = cv2.VideoCapture(3)

width = cap.get(3)
height = cap.get(4)

color = [0,0,255]
lower_red = np.array([0, 50, 70])
uppper_red = np.array([9, 255, 255])

def get_limits(color):

    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - -160, 50, 50
    upperLimit = hsvC[0][0][0] + 180, 200, 200

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit



while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color)
    
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (50,50,250), 5)

    cv2.imshow('frame', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()

cv2.destroyAllWindows()