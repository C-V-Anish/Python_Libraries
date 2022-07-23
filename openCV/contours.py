import cv2 as cv
import numpy as np

img=cv.imread('Images/img4.jpg')
cv.imshow('Original',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

#Converting to grayscale
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray_img)

#edge cascade
canny=cv.Canny(img,125,175)
cv.imshow('Canny',canny)

#Blur Image
blur_img=cv.GaussianBlur(canny,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur_img)

#find and rerturn contours of the image
#contours-the line joining all the points along the boundary of an image that are having the same intensity.
(contours,hierarchies)=cv.findContours(blur_img,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'No. of contours : {len(contours)}')

(ret,thresh)=cv.threshold(canny,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

cv.drawContours(blank,contours,-1,(255,255,255),1)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)