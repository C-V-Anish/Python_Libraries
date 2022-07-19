import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

'''img = cv.imread("Images\img2.jpg")
cv.imshow('Image',img)'''

#Paint the image
'''blank[:]=0,255,0
cv.imshow('Green',blank)

blank[0:100,10:110]=0,0,255
cv.imshow('Red',blank)'''

#Draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[0]//3,blank.shape[1]//3),(255,0,0),thickness=-1)
cv.imshow("Rectangle",blank)

cv.rectangle(blank,(0,0),(200,200),(255,0,0),thickness=-1)
cv.imshow("Rectangle",blank)

#Draw a circle
blank1 = np.zeros((500,500,3),dtype='uint8')
cv.circle(blank1,(blank1.shape[0]//2,blank1.shape[1]//2),50,(200,200,200),thickness=-1)
cv.imshow('Circle',blank1)

#Draw a line
cv.line(blank1,(0,0),(250,250),(255,255,255),thickness=4)
cv.imshow('Line',blank1)

#Write text on an image
cv.putText(blank1,'I am C.V.Anish',(250,250),cv.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)
cv.imshow("Text",blank1)

cv.waitKey(0)