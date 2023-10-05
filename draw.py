import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype="uint8")
cv.imshow("enBlanco",blank)
imagen=cv.imread('Photos/Cat.jpg')
#cv.imshow("Cat", imagen)

#pintar una imagen de cierto color
#blank[200:300, 400:500] = 0,255,0
#cv.imshow("enBlanco",blank)

#Dibujar un rectangulo
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow("Rectangulo",blank)

#Dibujar un circulo
cv.circle(blank,(0,0),40,(0,0,255), thickness=1)
cv.imshow("Circle",blank)

#Dibujar una linea
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=5)
cv.imshow("linea", blank)

#Añadir texto
cv.putText(blank,'Hola',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255))
cv.imshow("Saludo",blank)
cv.waitKey(0)
