import numpy as np 
import cv2

img=cv2.imread('lena.png',0)
cv2.imshow('lena_gray',img)
cv2.imwrite('lena_gray.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()