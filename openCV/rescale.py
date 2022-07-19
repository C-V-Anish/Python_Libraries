import cv2 as cv
from cv2 import INTER_AREA

img = cv.imread("Images\img3.jpg")
cv.imshow("Image",img)
                                                                #function to resize an Image,Video or Live Video
def rescaleFrame(frame,scale=0.75):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    
    dimensions=(width,height)
    
    return cv.resize(frame,dimensions,interpolation=INTER_AREA)

                                                                #function to resize a Live Video only
def changeRes(height,width):
    video.set(3,width)
    video.set(4,height)

resized_image=rescaleFrame(img)
cv.imshow("Image New",resized_image)



video=cv.VideoCapture('Videos\Vid1.mp4')

while (video.isOpened()):
    isTrue,frame=video.read()
    frame_resized=rescaleFrame(frame,scale=0.9)
    
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()