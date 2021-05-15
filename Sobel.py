# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:53:38 2021

@author: Ayla
"""

import cv2
import numpy as np

img = np.zeros((200,200,3), np.uint8)
cv2.rectangle (img,(20,20), (180,180), (50,50,50), -1)
cv2.rectangle (img,(40,40), (160,160), (100,100,100), -1)
cv2.rectangle (img,(60,60), (140,140), (150,150,150), -1)
cv2.rectangle (img,(80,80), (120,120), (200,200,200), -1)
cv2.rectangle (img,(100,100), (100,100), (250,250,250), -1)

cv2.imshow("Concentric Square",img)

laplacian = cv2.Laplacian(img,cv2.CV_64F)

vertical_kernel = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
horizontal_kernel = np.array([[1,2,1], [0,0,0], [-1,-2,-1]])

vertical = cv2.filter2D(laplacian, -1, vertical_kernel) 
horizontal = cv2.filter2D(laplacian, -1, horizontal_kernel)

cv2.imshow('Vertical Sobel',vertical)
cv2.imshow('Horizontal Sobel',horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()

