##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture4_class_exercises/red_cyan.py
##name: Tong Yi
##email: ty680@hunter.cuny.edu

import numpy as np
import matplotlib.pyplot as plt

#create an image from scratch
#let user input height and width 

#input function returns a string, int function convert the returned string to an int
height = int(input("Enter height of the image: "))
width = int(input("Enter width of the image: "))
img = np.zeros((height, width, 3)) #cannot omit () around height, width, 3
#height is number of rows
#width is number of columns
#3 is number of RGB channels, there are 3, one for red, one for green, one for blue
#np.zeros((height, width, 3)) create a height x width image with black background, the background is black since red/green/blue channels are all zero.

#set background to be cyan (green + blue)
img[:, :, 1] = 1 #use fraction as color, 100% green
img[:, :, 2] = 1

#TODO: set the horizontal half to be red
img[:height//2, :, 0] = 1
img[:height//2, :, 1] = 0
img[:height//2, :, 2] = 0

plt.imshow(img)
plt.show()

fileName = input("Enter saved file name: ")
plt.imsave(fileName, img)
