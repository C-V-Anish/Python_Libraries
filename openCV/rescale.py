import cv2 as cv
from cv2 import INTER_AREA

'''img = cv.imread("Images\img3.jpg")
cv.imshow("Image",img)'''

def rescaleFrame(frame,scale=0.75):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    
    dimensions=(width,height)
    
    return cv.resize(frame,dimensions,interpolation=INTER_AREA)

video=cv.VideoCapture('Videos\Vid1.mp4')

while (video.isOpened()):
    isTrue,frame=video.read()
    frame_resized=rescaleFrame(frame,scale=0.5)
    
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()