# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:27:24 2021

@author: Ayla
"""
import numpy as np
import cv2 

img =  cv2.imread('boat2.png')
cv2.imshow('Orijinal',img)

shape = img.reshape((-1,3))

shape = np.float32(shape)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv2.kmeans(shape, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)

final = center[label.flatten()]
final2 = final.reshape((img.shape))
cv2.imshow('res2',final2)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
import numpy as np
import cv2
img =  cv2.imread('/home/burakzdd/Desktop/rapor5/bb8.jpg')
cv2.imshow('Orjinal BB8',img)
#görüntü tekrar konumlandırılır
Z = img.reshape((-1,3))
# veri tipi np.float32 'ye dönüştürülür
Z = np.float32(Z)
# kriterleri, küme sayısı (K) tanımlanır ve k ortalama(means)değerleri uygulanır
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Grüntü tekraradan eski tipine (uint8'e) dönüştürülür ve görüntünün kümelendirilmiş hali oluşturulur
center = np.uint8(center)
res = center[label.flatten()]
KMimg = res.reshape((img.shape))
cv2.imshow('K-Means BB8',KMimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""