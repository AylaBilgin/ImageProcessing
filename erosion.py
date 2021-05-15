# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:40:57 2021

@author: Ayla
"""

import cv2
import numpy as np

img = cv2.imread('coin.png',0)

otsu_threshold, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)

cv2.imshow('Binary Image',img)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 2)

cv2.imshow('Erosion Image',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()



