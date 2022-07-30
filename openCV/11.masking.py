import cv2 as cv
import numpy as np

img=cv.imread("Images/img4.jpg")
cv.imshow("Original",img)

blank=np.zeros((img.shape[:2]),dtype="uint8")
cv.imshow("Blank",blank)

circle=cv.circle(blank.copy(),(250,250),250,(255,255,255),thickness=-1)
rectangle=cv.rectangle(blank.copy(),(40,40),(460,460),(255,255,255),thickness=-1)
weird_img=cv.bitwise_and(circle,rectangle)
cv.imshow("Weird",weird_img)

masked_img=cv.bitwise_and(img,img,mask=weird_img)
cv.imshow("Masked Image",masked_img)

cv.waitKey(0)