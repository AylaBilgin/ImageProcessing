# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:13:37 2021

@author: Ayla
"""

import cv2

img = cv2.imread('lena.png')

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
print(b.shape)
print(g.size)
print(r.size)
cv2.waitKey(0)
cv2.destroyAllWindows()




