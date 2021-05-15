# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:55:36 2021

@author: Ayla
"""

import cv2
import numpy as np
"""
img = np.zeros((200,200,3), np.uint8)
cv2.rectangle (img,(20,20), (180,180), (100,100,100), -1)
cv2.rectangle (img,(40,40), (160,160), (150,150,150), -1)
cv2.rectangle (img,(60,60), (140,140), (200,200,200), -1)
cv2.rectangle (img,(80,80), (120,120), (256,256,256), -1)
"""

img = cv2.imread('lena.png')
cv2.imshow("Concentric Square",img)
canny = cv2.Canny(img,20,170)
cv2.imshow('Canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

