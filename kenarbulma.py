# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:04:20 2021

@author: Ayla
"""

import cv2
import numpy as np

img = cv2.imread('rick.png',0)

otsu_threshold, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU,)

cv2.imshow('Binary Image',img)
 
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
erosion = cv2.erode(img,kernel,iterations = 1)

kenar1 = dilation-img
kenar2 = img-erosion

cv2.imshow('Edge1',kenar1)
cv2.imshow('Edge2',kenar2)
cv2.waitKey(0)
cv2.destroyAllWindows()




