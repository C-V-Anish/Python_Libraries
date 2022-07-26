#Basic functions of OpenCV
import cv2 as cv
from cv2 import INTER_AREA


img=cv.imread('Images\img6.jpg')
cv.imshow('Original',img)

#1.Convert an RGB image to Grayscale.
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

#2.Blur an Image
blur=cv.GaussianBlur(img,(9,9),cv.BORDER_WRAP)
cv.imshow('Blurred Image',blur)

#3.Edge Cascade
edge_cascade=cv.Canny(blur,125,175)
cv.imshow('IMAGE',edge_cascade)

#4.Dilate an Image - Opposite dilate
dilate_img=cv.dilate(edge_cascade,(7,7),iterations=3)
cv.imshow('Dilate',dilate_img)

#4.Erode an Image
erode_img=cv.erode(dilate_img,(3,3),iterations=3)
cv.imshow('Erode',erode_img)

#4.Resize an Image
resize_img=cv.resize(img,(1000,1000),interpolation=INTER_AREA)
cv.imshow('Image 2',resize_img)

#5.Crop an image
crop_img=img[100:200,200:400]
cv.imshow("Cropped Image",crop_img)

cv.waitKey(0)