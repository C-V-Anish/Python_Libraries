import cv2 as cv
import numpy as np

blank=np.zeros((500,500),dtype="uint8")
cv.imshow("Blank",blank)

rect=cv.rectangle(blank.copy(),(40,40),(460,460),(255,255,255),thickness=-1)
cv.imshow("Rectangle",rect)

circ=cv.circle(blank.copy(),(250,250),250,(255,255,255),thickness=-1)
cv.imshow("Circle",circ)

#Combines two images and show's their intersecting portion
bit_and=cv.bitwise_and(rect,circ)
cv.imshow("Bitwise And",bit_and)

#Combines two images and show's their intersecting as well as non-intersecting part
bit_or=cv.bitwise_or(rect,circ)
cv.imshow("Bitwise_Or",bit_or)

#Combines two images and show's their non-intersecting part
bit_xor=cv.bitwise_xor(rect,circ)
cv.imshow("Bitwise Xor",bit_xor)

#Shows the complement part of a particular image
bit_notr=cv.bitwise_not(rect)
cv.imshow("Not Rect",bit_notr)
bit_notc=cv.bitwise_not(circ)
cv.imshow("Not Circ",bit_notc)

cv.waitKey(0)