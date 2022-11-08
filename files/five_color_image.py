##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture6_class_exercises/five_color_image.py
#display an image with 5 colors: red, green, blue, black and yellow
##name: csci teaching staff 
import numpy as np
import matplotlib.pyplot as plt

height= 20
width = 32
img = np.zeros((height, width, 3)) #3: depth for rgb
img[:height//2, :width//2, 0] = 1 #top left red
#same as img[:height//2, :width//2] = [1, 0, 0]

img[height//2:, :width//2, 1] = 1 #bottom left green
#same as img[height//2:, :width//2] = [0, 1, 0]

img[:height//2:2, width//2:, 2] = 1 #color of top right?

img[height//2:, width//2::2, ] = [1, 1, 0]
#color of bottom right?

#plt.imshow(img)
plt.imshow(img, interpolation='nearest', extent=[0,width,height,0]) #compared with plt.imshow(img), this statement can make x-axis and y-axis ticks aligned to the edge of img nicely.
plt.yticks(np.arange(0, height+1, 5)) #set up the yticks separated by 5. 
plt.show()

