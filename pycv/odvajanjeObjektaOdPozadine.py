import cv2 as cv
import numpy as np

img = cv.imread('gradient.png', 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) #ako je vece od 127 onda je 255, u suprotnom nula
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) # do 127 se nece mijenjati, posle toga se mijenjaju


cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)

cv.waitKey(5000)
cv.destroyAllWindows()