# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:43:04 2021

@author: Ayla
"""

import cv2
from matplotlib import pyplot as plt

image = cv2.imread('boat.jpg',0)
plt.hist(image.ravel(),256,[0,256]) #img.ravel görüntüyü 1D yapar.
plt.show()
img = image.copy()
otsu_threshold, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)

print("Obtained threshold: ", otsu_threshold)

plt.hist(img.ravel(),256,[0,256]) #img.ravel görüntüyü 1D yapar.
plt.show()

plt.imshow(img,'gray')
plt.show()



"""
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("boat2.png") # oku
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # bgr den grayscale yap

im1 = img.copy()
ret,im1 = cv2.threshold(im1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # imge otsu thresholding e maruz kaliyor
print (ret)

plt.figure(1)
plt.subplot(121)
plt.imshow(img,cmap='gray')

plt.subplot(122)
plt.imshow(im1,cmap='gray')
plt.show() # goster
"""