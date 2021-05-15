# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:56:18 2021

@author: Ayla
"""

import cv2
import numpy as np

def GradientMagnitude(img):
    ddepth = cv2.CV_32F
    sobel_x = cv2.Sobel(img, ddepth, 1, 0)
    sobel_y = cv2.Sobel(img, ddepth, 0, 1)
    dxabs = cv2.convertScaleAbs(sobel_x)
    dyabs = cv2.convertScaleAbs(sobel_y)
    mag = cv2.addWeighted(dxabs, 0.5, dyabs, 0.5, 0)
    return mag
"""
img = np.zeros((200,200,3), np.uint8)
cv2.rectangle (img,(20,20), (180,180), (100,100,100), -1)
cv2.rectangle (img,(40,40), (160,160), (150,150,150), -1)
cv2.rectangle (img,(60,60), (140,140), (200,200,200), -1)
cv2.rectangle (img,(80,80), (120,120), (256,256,256), -1)
"""
img = cv2.imread('lena.png',0)
mag = GradientMagnitude(img)
cv2.imshow("kareler",mag)
cv2.waitKey(0)
cv2.destroyAllWindows()