#import OpenCV
import cv2

#import Unique identification number
import uuid

img = cv2.VideoCapture(0)
width = int(img.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(img.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = img.read()
    imgname = './images/nospecs/{}.jpg'.format(str(uuid.uuid1()))
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

img.release()
img.destroyallwindows()