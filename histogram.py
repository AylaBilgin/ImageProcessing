#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2 
import matplotlib.pyplot as plt

def hist_plot(img): 
    count =[] 
    r = [] 
    for k in range(0, 256): 
        r.append(k) 
        count1 = 0
        for i in range(m): 
            for j in range(n): 
                if img[i, j]== k: 
                    count1+= 1
        count.append(count1)    
    return (r, count) 
  
img = cv2.imread('castle.png', 0) 
  
m,n= img.shape
r1, count1 = hist_plot(img) 
  
plt.stem(r1, count1) 
plt.xlabel('Yoğunluk Değeri') 
plt.ylabel('Piksel Sayısı') 
plt.title('Görüntünün Histogramı') 
plt.show()


