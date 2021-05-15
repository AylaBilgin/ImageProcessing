import cv2
import numpy as np

img= cv2.imread("lena_gray.png")

div = 64
quantized = img // div * div + div // 2
cv2.imshow('Lena_2bitquantized.jpg', quantized)

cv2.waitKey(0)
cv2.destroyAllWindows()