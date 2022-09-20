##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture4_class_exercises/vertical_red_blue_strips.py
##name: CSci 127 teaching staff 
##email: ty680@hunter.cuny.edu

import numpy as np
import matplotlib.pyplot as plt

#input height and width
height = int(input("Enter height: "))
width = int(input("Enter width: "))

#create a height x width image with blue background
img = np.zeros((height, width, 3))
img[:, : , 2] = 1 #blue channel of the whole image is 1.

#draw red vertical lines in even indices
#set red channel of vertical stripes with even indices to be 1,
#::2 is in the second parameter of img slicing, 
#::2 tells us how to slice the second dimension, ie columns,
#or vertically, in image img.
#::2 is the same as 0:width:2,
#Nothing is before the leftmost : in ::2 means to start from 0.
#Default start is 0, when omitted, default value is used. 
#Nothing is before the two :'s in ::2 means to end by width,
#the number of columns in image img.
#Default stop (ie, end) is width, when omitted, default value is used.
#2 in ::2 means to step by 2.
#Suppose width is 20,
#then ::2 uses indices 0, 2, 4, ..., 18.
img[:, ::2, 0] = 1

#NOTE that by img[:, :, 2] = 1 in background setup,
#every pixel in the picture is set to be blue,
#with img[:, ::2, 0] = 1, 
#the red channel of vertical even strips in [0, width), 
#where 0 is included but not width,
#is set to be 1,
#So visually these vertical even strips are blue + red = purple.
#If we want to have pure red in those vertical even strips,
#we need to remove its blue channel, that is, set its blue channel to be zero.
img[:, ::2, 2] = 0 

#show img
plt.imshow(img)
plt.show()
