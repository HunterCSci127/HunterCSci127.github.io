##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture10_class_exercises/maximum3.py
##name: CSci127 teaching staff

nums = [1, 4, 10, 6, 5, 42, 9, 8, 12]

size = len(nums)
if size == 0:
   print("The list is empty and does not have a maximum")
   exit(0) #cannot use return since this is not an function

maxNum = nums[0]
for i in range(1, size):
    if nums[i] > maxNum:
       maxNum = nums[i] 

print(maxNum)
