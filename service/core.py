import cv2
import numpy as np
import math


def get_area(real_height, real_width, file):
    im = cv2.imread(file, 0)
    
    img_height, img_width = im.shape
    
    meters_per_pixel_height = real_height / img_height
    meters_per_pixel_width = real_width / img_width
    print(meters_per_pixel_height * meters_per_pixel_width)

    contours, hierarchy = cv2.findContours(im.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    out = np.zeros_like(im)

    cv2.drawContours(out, contours, -1, 255, -1)

    return math.sqrt(np.count_nonzero(out) * meters_per_pixel_height * meters_per_pixel_width)
