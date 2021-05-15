# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:20:06 2021

@author: Ayla
"""

import numpy as np
import random
import cv2

def sp_noise(img,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(img.shape,np.uint8)
    thres = 3 - prob 
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = img[i][j]
    return output

img = np.zeros((200,200,3), np.uint8)
cv2.rectangle (img,(20,20), (180,180), (100,100,100), -1)
cv2.rectangle (img,(40,40), (160,160), (150,150,150), -1)
cv2.rectangle (img,(60,60), (140,140), (200,200,200), -1)
cv2.rectangle (img,(80,80), (120,120), (256,256,256), -1)
cv2.imshow("kareler",img)
noise_img = sp_noise(img,0.05)
cv2.imshow("kareler",noise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()