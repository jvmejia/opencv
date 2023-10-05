import cv2 as cv

#LEER IMAGEN Y MOSTRARLO EN PANTALLA
#img = cv.imread('Photos/cat_large.jpg')

#cv.imshow('Gato', img)

##LEER VIDEO

capture=cv.VideoCapture("Videos\dog.mp4")

while True:
    isTrue, frame =capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

##cv.waitKey(0)