import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread('Photos/park.jpg')
cv.imshow("Normal", img)
#BGR TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gris", gray)

#BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#BGR TO L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

#BGR TO RGB
RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", RGB)

#HSV TO BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)
cv.waitKey(0)