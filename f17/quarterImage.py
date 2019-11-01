#Name:  CSci 127 Teaching Staff
#Date:  Fall 2017
#This program loads an image, displays it, and then creates and displays
#    a new image that is only the upper left corner.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt  
import numpy as np

img = plt.imread('csBridge.png')   #Read in image from csBridge.png
plt.imshow(img)		           #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

height = img.shape[0]              #Get height
width = img.shape[1]               #Get width

img2 = img[:int(height/2), :int(width/2)]    #Crop to upper left corner

plt.imshow(img2)                   #Load our new image into pyplot
plt.show()                         #Show the image (waits until closed to continue)
