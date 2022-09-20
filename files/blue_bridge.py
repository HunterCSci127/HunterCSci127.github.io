##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture4_class_exercises/blue_bridge.py
##name: CSci 127 teaching staff 

#install using pip3 install numpy
import numpy 
#install using pip3 install matplotlib
import matplotlib.pyplot as plt 

#put csBridge.png in the same folder (directory) 
#as current python source code
#img is a 3-dimensional array if png file is colored picture,
#img is a 2-dimensional array if png file is 
#a black and write picture
img = plt.imread("csBridge.png")

#the following two statements show csBridge.png
plt.imshow(img)
plt.show()

#copy img to img2
img2 = img.copy()
#TODO: remove the red and green channel of img2,
#ie, set these two channel to be zero.
#TODO: challenge: set the middle half in height
#to be blue, while keeping the rest the original color
height = img2.shape[0] #number of rows
width = img2.shape[1] #number of columns
img2[height//4:height*3//4:2, :, 0] = 0
img2[height//4:height*3//4:2, :, 1] = 0

#display img2
plt.imshow(img2)
plt.show()

plt.imsave("csBridge_blue.png", img2)
