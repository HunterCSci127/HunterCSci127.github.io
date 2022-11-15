##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture10_class_exercises/maximum2.py
##name: CSci127 teaching staff

import sys #use sys.maxsize

nums = [1, 4, 10, 6, 5, 42, 9, 8, 12]
#for discussion on maximum and minimum integer in python,
#google "maximum int python"
#see https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
maxNum = -sys.maxsize -1 
print('maximum number =', maxNum)
for n in nums:
    if n > maxNum:
       maxNum = n

print(maxNum)
