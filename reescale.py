import cv2 as cv

def changeRes(width, height):
    capture.set(3, height)
    capture.set(4,height)

def reescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


img=cv.imread("Photos/cat.jpg")
cv.imshow('gato', img)
rezised_image = reescaleFrame(img,0.2)
cv.imshow('gatochikito', rezised_image)
capture=cv.VideoCapture("Videos\dog.mp4")



while True:
    isTrue, frame =capture.read()
    frame_resized = reescaleFrame(frame,0.2) 
    cv.imshow('video',frame)
    cv.imshow('videochikito', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
