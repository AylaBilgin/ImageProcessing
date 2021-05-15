# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 02:27:44 2021

@author: Ayla
"""

import cv2
import numpy as np

image = cv2.imread('morty.png')
cv2.imshow('original',image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

shape = np.float32(image.reshape(-1,3))

numberofClusters = 2

stop = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.1)

ret, label, clusters = cv2.kmeans(shape, numberofClusters, None, stop, 10, cv2.KMEANS_RANDOM_CENTERS)

clusters = np.uint8(clusters)

img = clusters[label.flatten()]

img2 = img.reshape((image.shape))

cv2.imshow('morty',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



