# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 01:18:48 2021

@author: Ayla
"""

import cv2

img = cv2.imread ('lena.png', 0)

ret, eşik1 = cv2.threshold (img, 127,255, cv2. THRESH_BINARY )
ret, eşik2 = cv2.threshold (img, 127,255, cv2. THRESH_BINARY_INV )
ret, eşik3 = cv2.threshold (img, 127,255, cv2. THRESH_TRUNC )
ret, eşik4 = cv2.threshold (img, 127,255, cv2. THRESH_TOZERO )
ret, eşik5 = cv2.threshold (img, 127,255, cv2. THRESH_TOZERO_INV )

cv2.imshow('Binary',eşik1)
cv2.imshow('BinaryInv',eşik2)
cv2.imshow('Trunc',eşik3)
cv2.imshow('Tozero',eşik4)
cv2.imshow('TozeroInv',eşik5)

cv2.waitKey(0)
cv2.destroyAllWindows()

