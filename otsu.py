# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:19:27 2021

@author: Ayla
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('coin.png', 0)
img = image.copy()

bins_num = 256

hist, bin_edges = np.histogram(image, bins=bins_num)
hist = np.divide(hist.ravel(), hist.max())

bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.

weight1 = np.cumsum(hist)
weight2 = np.cumsum(hist[::-1])[::-1]

mean1 = np.cumsum(hist * bin_mids) / weight1
mean2 = (np.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]
 
inter_class_variance = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2
index_of_max_val = np.argmax(inter_class_variance)

threshold = bin_mids[:-1][index_of_max_val]
otsu_threshold,img = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)

print ("{} {}".format(threshold,otsu_threshold))

plt.figure(1)
plt.subplot(121)
plt.imshow(image,cmap='gray')

plt.subplot(122)
plt.imshow(img,cmap='gray')
plt.show()


"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('coin.png', 0)
img = image.copy()

# Set total number of bins in the histogram
bins_num = 256

# Get the image histogram
hist, bin_edges = np.histogram(image, bins=bins_num)

hist = np.divide(hist.ravel(), hist.max())
 
# Calculate centers of bins
bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.

# Iterate over all thresholds (indices) and get the probabilities w1(t), w2(t)
weight1 = np.cumsum(hist)

weight2 = np.cumsum(hist[::-1])[::-1]

# Get the class means mu0(t)
mean1 = np.cumsum(hist * bin_mids) / weight1

# Get the class means mu1(t)
mean2 = (np.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]
 
inter_class_variance = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

# Maximize the inter_class_variance function val
index_of_max_val = np.argmax(inter_class_variance)

threshold = bin_mids[:-1][index_of_max_val]

#otsu_threshold, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
otsu_threshold,img = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)

print("{} {}".format(threshold,otsu_threshold) )

"""

plt.figure(1)
plt.subplot(121)
plt.imshow(image,cmap='gray')

plt.subplot(122)
plt.imshow(img,cmap='gray')
plt.show()


