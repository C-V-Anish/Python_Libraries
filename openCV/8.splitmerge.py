import cv2 as cv
import numpy as np

img=cv.imread("Images/img2.jpg")
cv.imshow("Original",img)

blank=np.zeros(img.shape[:2],dtype="uint8")

B,G,R=cv.split(img)
cv.imshow("Blue",B)
cv.imshow("Red",R)
cv.imshow("Green",G)

print(img.shape)
print(B.shape)
print(G.shape)
print(R.shape)

merge_img=cv.merge([B,G,R])
cv.imshow("Merge Image",merge_img)

blue=cv.merge([B,blank,blank])
green=cv.merge([blank,G,blank])
red=cv.merge([blank,blank,R])

cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

cv.waitKey(0)