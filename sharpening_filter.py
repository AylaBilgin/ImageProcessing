# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:36:50 2021

@author: Ayla



import cv2
import numpy as np

img = cv2.imread('lena.png',0)
img = cv2.resize(img , (400 , 400))
cv2.imshow('lena',img)

kernel = np.array([[0 , -1 , 0] ,
                   [-1 , 4 , -1] ,
                   [0 , -1 , 0]])

sharp_img = cv2.filter2D(img , -1 , kernel = kernel)
zero_padding1 = cv2.copyMakeBorder(sharp_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
cv2.imshow('lena_sharpening',zero_padding1)

kernel1 = np.array([[0,-1,0], [0,0, 0], [0,1,0]])
kernel2 = np.array([[0,0,0], [1,0,-1], [0,0,0]])
vertical = cv2.filter2D(sharp_img, -1, kernel1) + 128
horizontal = cv2.filter2D(sharp_img, -1, kernel2) + 128
zero_padding2 = cv2.copyMakeBorder(vertical, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
zero_padding3 = cv2.copyMakeBorder(horizontal, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
cv2.imshow('lena_vert',zero_padding2)
cv2.imshow('lena_hor',zero_padding3)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

import cv2
import numpy as np

img = cv2.imread('lena.png')
cv2.imshow('original',img)

kernel_upperleft = np.array([[0,1,0], [1,-4,1], [0,1,0]])
kernel_upperright = np.array([[1,1,1], [1,-8,1], [1,1,1]])
kernel_bottomleft = np.array([[0,-1,0], [-1,4,-1], [0,-1,0]])
kernel_bottomright = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])

output_1 = cv2.filter2D(img, -1, kernel_upperleft)
output_2 = cv2.filter2D(img, -1, kernel_upperright)
output_3 = cv2.filter2D(img, -1, kernel_bottomleft)
output_4 = cv2.filter2D(img, -1, kernel_bottomright)

zero_padding1 = cv2.copyMakeBorder(output_1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
zero_padding2 = cv2.copyMakeBorder(output_2, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
zero_padding3 = cv2.copyMakeBorder(output_3, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
zero_padding4 = cv2.copyMakeBorder(output_4, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
cv2.imshow('lena1',zero_padding1)
cv2.imshow('lena2',zero_padding2)
cv2.imshow('lena3',zero_padding3)
cv2.imshow('lena4',zero_padding4)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""
import cv2
import numpy as np

img = cv2.imread('lena.png')
cv2.imshow('original',img)

kernel_upperleft = np.array([[0,1,0], [1,-4,1], [0,1,0]])
kernel_upperright = np.array([[1,1,1], [1,-8,1], [1,1,1]])
kernel_bottomleft = np.array([[0,-1,0], [-1,4,-1], [0,-1,0]])
kernel_bottomright = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])

output_1 = cv2.filter2D(img, -1, kernel_upperleft)
output_2 = cv2.filter2D(img, -1, kernel_upperright)
output_3 = cv2.filter2D(img, -1, kernel_bottomleft)
output_4 = cv2.filter2D(img, -1, kernel_bottomright)

zero_padding1 = cv2.copyMakeBorder(output_1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
zero_padding2 = cv2.copyMakeBorder(output_2, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
zero_padding3 = cv2.copyMakeBorder(output_3, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
zero_padding4 = cv2.copyMakeBorder(output_4, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)

laplacian_1 = cv2.Laplacian(zero_padding1, cv2.CV_64F)
laplacian_2 = cv2.Laplacian(zero_padding2, cv2.CV_64F)
laplacian_3 = cv2.Laplacian(zero_padding3, cv2.CV_64F)
laplacian_4 = cv2.Laplacian(zero_padding4, cv2.CV_64F)

cv2.imshow('lena1',laplacian_1)
cv2.imshow('lena2',laplacian_2)
cv2.imshow('lena3',laplacian_3)
cv2.imshow('lena4',laplacian_4)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
