##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture4_class_exercises/H_logo.py
##name: CSci 127 teaching staff 

import numpy as np
import matplotlib.pyplot as plt

#create a white background 10 x 10 image to draw H logo
img = np.ones((10, 10, 3))

#H is in purple color
#the leftmost 3 vertical lines represents left vertical line in H
img[:, 0:3, 1] = 0 

#the rightmost 3 vertical lines represents right vertical line in H
img[:, 7:, 1] = 0 

#Use your fingers to find out the middle two lines. 
#the middle line in H is in the fifth and sixth horizontal lines, ie, indices 4 and 5. 
img[4:6, :, 1] = 0 

#show image img
plt.imshow(img)
plt.show()
