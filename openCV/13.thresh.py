import numpy as np
import cv2 as cv

img = cv.imread("Images/img5.jpg")
cv.imshow("original",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grayscale",gray)

#Simple Thresholding
threshold,thresh=cv.threshold(gray,225,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

threshold,thresh_inv=cv.threshold(gray,225,255,cv.THRESH_BINARY_INV)
cv.imshow('Thresh Inv',thresh_inv)

#adaptive thresholding

ad_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('Thresh Inv1',ad_thresh)

cv.waitKey(0)
