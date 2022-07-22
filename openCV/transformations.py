import cv2 as cv
import numpy as np

img=cv.imread('Images\img4.jpg')

cv.imshow('Original',img)

#Translation - shifting image along x and y axes
#+x -> right,-x -> left,-y -> down,-y -> up
def translate(img,x,y):
    TransArr=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,TransArr,dimensions)

trans_img=translate(img,-100,-100)
cv.imshow('Translated',trans_img)

#Rotation
#-angle->clockwise,+angle->counter-clockwise
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rot_img=rotate(img,60,)
cv.imshow("Rotated",rot_img)

rot_rot_img=rotate(rot_img,60)
cv.imshow("Rotated",rot_rot_img)

#Resize an Image
resize_img=cv.resize(img,(100,100))
cv.imshow("Resized",resize_img)

#Flipping an image
flip_img=cv.flip(img,-1)
cv.imshow("Flipped",flip_img)

#Crop an Image
crop_img=img[100:200,300:400]
cv.imshow("Cropped",crop_img)

cv.waitKey(0)
