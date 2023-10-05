import cv2 as cv
imagen=cv.imread('Photos/park.jpg')
cv.imshow("Parque", imagen)

#CONVERTIR IMAGEN BGR A IMAGEN EN ESCALA DE GRISES
gris=cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)
#cv.imshow("Gris",gris)

#Blur
blur=cv.GaussianBlur(imagen,(7,7), cv.BORDER_DEFAULT)
#cv.imshow("Blureado",blur)

#Edge Cascade
canny = cv.Canny(blur,125,175)
#cv.imshow("Canny", Canny)

#Dilated
dilated= cv.dilate(canny, (7,7),iterations=1)
cv.imshow("dilated", dilated)

#Eroding
eroded=cv.erode(dilated,(3,3), iterations=1)
cv.imshow("eroded", eroded)

#Resize Image
resized = cv.resize(imagen,(1080,720), interpolation=cv.INTER_CUBIC)
cv.imshow("Chiquito",resized)

#Crop Image
cropped = imagen[50:200, 200:400]
cv.imshow("Cortado", cropped)
cv.waitKey(0)
