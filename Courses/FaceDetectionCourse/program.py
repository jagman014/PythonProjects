# uses python 2.7
import cv2 as cv

original_image = cv.imread('test_image.jpg')
greyscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

detected_faces = face_cascade.detectMultiScale(greyscale_image, 1.3)

for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )

img = cv.resize(original_image, (0, 0), fx=1, fy=1)
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
