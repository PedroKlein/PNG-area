import cv2
import numpy as np
import math

realHeight = 1
realWidth = 2

im = cv2.imread('test2.png', 0)

imgHeight, imgWidth = im.shape
pixelsPerMetricHeigth = realHeight / imgHeight
pixelsPerMetricWidth = realWidth / imgWidth
print(pixelsPerMetricHeigth * pixelsPerMetricWidth)

contours, hierarchy = cv2.findContours(im.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

out = np.zeros_like(im)

cv2.drawContours(out, contours, -1, 255, -1)

#Result
print(math.sqrt(np.count_nonzero(out) * pixelsPerMetricHeigth * pixelsPerMetricWidth))

cv2.waitKey(0)
cv2.destroyAllWindows()