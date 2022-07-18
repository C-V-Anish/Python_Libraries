import cv2 as cv

#Reading Images

'''img=cv.imread('Images\img6.jpg') 

cv.imshow('Image',img)  

cv.waitKey(0)'''

#Reading Videos

video=cv.VideoCapture('Videos\Vid1.mp4')

while (video.isOpened()):
    isTrue,frame=video.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()
