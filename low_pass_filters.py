# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:58:53 2021

@author: Ayla
"""

"""
import cv2
import numpy as np

img = cv2.imread('lena_noisy.png')
cv2.imshow('original_image',img)
kernel = np.ones((3, 3), np.float32) / 9 
mask = cv2.filter2D(img, -1, kernel)
zero_padding = cv2.copyMakeBorder(mask, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
cv2.imshow('lena',zero_padding)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""


import cv2
import numpy as np

img = cv2.imread('lena_noisy.png')
cv2.imshow('original_image',img)
kernel = (np.array([[1 , 2 , 1] ,[2 , 4 , 2] ,[1 , 2 , 1]])) / 16
mask = cv2.filter2D(img, -1, kernel)
zero_padding = cv2.copyMakeBorder(mask, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
cv2.imshow('lena',zero_padding)
cv2.waitKey(0)
cv2.destroyAllWindows()


