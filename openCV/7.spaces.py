import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread("Images/img3.jpg")
cv.imshow("Original",img)

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale",gray_img)

#Converting RGB image to HSV image
hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV Image",hsv_img)

#Converting RGB image to LAB image
lab_img=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB Image",lab_img)

'''#Converting BGR to RGB Image
rgb_img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb_img)

plt.imshow(img)
plt.show()'''

l2b_img=cv.cvtColor(lab_img,cv.COLOR_LAB2BGR)
cv.imshow("Lab-->BGR",l2b_img)

h2b_img=cv.cvtColor(hsv_img,cv.COLOR_HSV2BGR)
cv.imshow("HSV-->BGR",h2b_img)

g2b_img=cv.cvtColor(gray_img,cv.COLOR_GRAY2BGR)
cv.imshow("Gray-->BGR",g2b_img)

cv.waitKey(0)