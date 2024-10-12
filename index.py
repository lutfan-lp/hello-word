import numpy as np
import cv2 as cv

gambar = cv.imread('mine.jpg')

cv.imshow ('gambar 1', gambar)

cv.waitKey(0)
cv.destroyAllWindows()