import cv2 as cv
KERNEL_SIZE = (3,3)
img = cv.imread('Photos/cats.jpg')
cv.imshow('Original', img)

#averaging
average = cv.blur(img,KERNEL_SIZE)
cv.imshow('Average blur', average)

#Gausian Blur
gauss = cv.GaussianBlur(img, KERNEL_SIZE, 0 )
cv.imshow('Gaussian Blur', gauss)

#Median blur
median = cv.medianBlur(img,3)
cv.imshow('Median Blur', median)

#Bilateral Bluring
bilateral = cv.bilateralFilter(img, 5 , 15, 15)
cv.imshow('Bilateral Blur', bilateral)
cv.waitKey(0)