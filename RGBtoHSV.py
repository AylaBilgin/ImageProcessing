# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:50:54 2021

@author: Ayla
"""
"""
import cv2

image = cv2.imread('lena.png')
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
cv2.imshow('Original image',image)
cv2.imshow('HSV image', hsvImage)
   
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
import cv2
import numpy as np

image = cv2.imread('lena.png')
boundaries = [
    ([160, 0, 0], [180, 255, 255]),
    ([20, 0, 0], [30, 255, 255])]

converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
     
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(converted, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    
cv2.imshow("images", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

import cv2
   
img = cv2.imread('lena.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
cv2.imshow('RGB Image',img)
cv2.imshow('HSV Image', hsv)
print(img.shape)
print(hsv.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()