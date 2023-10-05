import cv2 as cv
import numpy as np

# Lee la imagen 'cats.jpg' y la guarda en la variable 'img'
img = cv.imread('Photos/cats.jpg')

# Muestra la imagen en una ventana con el título "Imagen"
cv.imshow("Imagen", img)

# Crea una imagen en blanco del mismo tamaño que la imagen 'img'
# dtype='uint8' especifica el tipo de datos de la imagen en blanco
blank =  np.zeros(img.shape[:2], dtype='uint8')

# Muestra la imagen en blanco en una ventana con el título "Imagen en blanco"
cv.imshow('Imagen en blanco', blank)

# Crea una máscara circular en la imagen en blanco
# El centro de la máscara está en el centro de la imagen 'img'
# El radio de la máscara es 100 píxeles
# El valor 255 especifica que la máscara es completamente blanca
# El valor -1 especifica que la máscara es sólida (no tiene agujeros)
mask=cv.circle(blank,(img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# Muestra la máscara en una ventana con el título "mask"
cv.imshow("mask", mask)

# Aplica la máscara a la imagen 'img' usando la operación bitwise AND
# La función bitwise_and toma dos imágenes y una máscara como entrada
# La máscara especifica qué píxeles de la imagen deben ser procesados
# Los píxeles que corresponden a valores de 0 en la máscara se establecen en 0 en la imagen de salida
masked_image = cv.bitwise_and(img,img, mask=mask)

# Muestra la imagen enmascarada en una ventana con el título "Imagen enmascarada"
cv.imshow("Imagen enmascarada", masked_image )

# Espera a que el usuario presione cualquier tecla
cv.waitKey(0)