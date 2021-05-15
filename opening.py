# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:56:20 2021

@author: Ayla
"""

import cv2
import numpy as np

img = cv2.imread('rick.png',0)

otsu_threshold, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU,)

cv2.imshow('Binary Image',img)

kernel = np.ones((7,7),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening Image',opening)

erosion = cv2.erode(opening,kernel,iterations = 2)
cv2.imshow('Opening 2 Image',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

