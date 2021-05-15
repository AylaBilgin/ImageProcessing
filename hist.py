"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("lena.png")
imgray=cv2.imread("lena_gray.png") 

img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgray=cv2.cvtColor(imgray, cv2.COLOR_BGR2GRAY)

size_y=img.shape[0]
size_x=img.shape[1]
size_a=imgray.shape[0]
size_b=imgray.shape[1]

flattened=img.reshape([size_x*size_y])
flat=imgray.reshape([size_a*size_b])

rhist,_,_=plt.hist(flattened, bins=256)
plt.show()
rhist,_,_=plt.hist(flat, bins=256)
plt.show()


import cv2
import numpy as np
from matplotlib import pyplot as plt

cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']  
data = [23, 17, 35, 29, 12, 41]   

fig = plt.figure(figsize =(10, 7)) 
plt.pie(data, labels = cars)   

plt.show() 

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.bar(langs,students)
plt.show()

import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y)
plt.show()


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()

"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('lena.png')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_image[40:100,80:400]=0
cv2.imshow("Lena image - gray scale",gray_image)
plt.imshow(gray_image)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

