import cv2 as cv


img=cv.imread("Images/img1.jpg")
cv.imshow("Original",img)

#Average Blur-the resultant pixel intensity of a block is averaged to that of all the pixel intensities of the block surrounding the block in the image.
avg_img=cv.blur(img,(3,3))
cv.imshow("Avg Blur",avg_img)

#Gaussian Blur
gauss_img=cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gauss Blur",gauss_img)

#Median Blur-similar as that of the Average Blur , the only change being instead of averaging the pixel intensities,the median of all the intensities are calculated
med_img=cv.medianBlur(img,3)
cv.imshow("Median Blur",med_img)

#Bi-Lateral Blur
bi_img=cv.bilateralFilter(img,5,15,15)
cv.imshow("Bi-Lateral Blur",bi_img)

cv.waitKey(0)