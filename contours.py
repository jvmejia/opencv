import cv2 as cv
import numpy as np

COLOR_ROJO=(0,0,255)
img = cv.imread("Photos/cats.jpg")
cv.imshow("Imagen base", img)

blank=np.zeros(img.shape, dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gris", gray)
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow("Borroso", blur)

###Encuentra los contornos en la imagen utilizando el operador Canny y almacena los resultados en las variables contours y hierarchies.
canny = cv.Canny(blur, 125, 175)
cv.imshow("canny",canny)


# Aplicar umbralización a la imagen en escala de grises 'gray'.
# Cualquier píxel con un valor menor o igual a 125 se convierte en negro (0),
# y cualquier píxel con un valor mayor a 125 se convierte en blanco (255).
#ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
#cv.imshow("Threshold", thresh)


countours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(countours)} coutour(s) found' )

cv.drawContours(blank, countours, -1, COLOR_ROJO, 1)
cv.imshow('Contornos dibujados', blank)
cv.waitKey(0)