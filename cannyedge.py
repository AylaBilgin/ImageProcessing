# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:00:08 2021

@author: Ayla
"""

import cv2
import numpy as np


img = np.zeros((200,200,3), np.uint8)
cv2.rectangle (img,(20,20), (180,180), (100,100,100), -1)
cv2.rectangle (img,(40,40), (160,160), (150,150,150), -1)
cv2.rectangle (img,(60,60), (140,140), (200,200,200), -1)
cv2.rectangle (img,(80,80), (120,120), (256,256,256), -1)
cv2.imshow('orijinal',img)


kernel = np.array([[1,4,7,4,1], [4,16,26,16,4], [7,26,41,26,7], [4,16,26,16,4], [1,4,7,4,1]]) / 273
mask = cv2.filter2D(img, -1, kernel,0)
cv2.imshow('gauss',mask)

def GradientMagnitude(img):
    ddepth = cv2.CV_32F
    sobel_x = cv2.Sobel(img, ddepth, 1, 0)
    sobel_y = cv2.Sobel(img, ddepth, 0, 1)
    dxabs = cv2.convertScaleAbs(sobel_x)
    dyabs = cv2.convertScaleAbs(sobel_y)
    mag = cv2.addWeighted(dxabs, 0.5, dyabs, 0.5, 0)
    return mag
mag = GradientMagnitude(mask)
cv2.imshow("gradyan",mag)

NMS = np.array([[0,0,0],[0,1,-1],[0,0,0]])
mask2 = cv2.filter2D(mag, -1, NMS,0)
cv2.imshow("nms",mask2)

retval, thresh = cv2.threshold(mask2, mask2.min(), mask2.max() , cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

