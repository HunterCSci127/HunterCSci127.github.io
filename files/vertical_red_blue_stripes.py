##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture4_class_exercises/vertical_red_blue_stripes.py
##name: CSci 127 teaching staff 
##email: ty680@hunter.cuny.edu

import numpy as np
import matplotlib.pyplot as plt

#input height and width
height = int(input("Enter height: "))
width = int(input("Enter width: "))

#create a height x width image with blue background
img = np.zeros((height, width, 3))
img[:, : , 2] = 1

#draw red vertical lines in even indices
img[:, ::2, 0] = 1

#show img
plt.imshow(img)
plt.show()
