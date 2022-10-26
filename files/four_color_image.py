##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture6_class_exercises/four_color_image.py
##name: csci teaching staff 
import numpy as np
import matplotlib.pyplot as plt

height= 20
width = 30
img = np.zeros((height, width, 3)) #3: depth for rgb
img[:height//2, :width//2, 0] = 1 #top left red
#same as img[:height//2, :width//2] = [1, 0, 0]

img[height//2:, :width//2, 1] = 1 #bottom left green
#same as img[height//2:, :width//2] = [0, 1, 0]

img[:height//2:2, width//2:, 2] = 1 #color of top right?

img[height//2:, width//2::2, ] = [1, 1, 0]
#color of bottom right?

plt.imshow(img)
plt.show()

