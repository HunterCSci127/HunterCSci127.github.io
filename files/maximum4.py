##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture10_class_exercises/maximum4.py
##name: CSci127 teaching staff

#import math #nan

def maximum(nums):
    size = len(nums)

    if size == 0:
       #print("The list is empty and does not have a maximum")
       #exit(0) #cannot use return since this is not an function
       return float('nan') #nan means Not a Number
       #int('nan') does not work, since int in python is not bounded.

    maxNum = nums[0]
    for i in range(1, size):
        if nums[i] > maxNum:
           maxNum = nums[i] 

    return maxNum

def main():
    nums = []
    maxNum = maximum(nums)
    print("maximum element of", nums, "is", maxNum)

    nums2 = [1, 4, 10, 6, 5, 42, 9, 8, 12]
    maxNum2 = maximum(nums2)
    print("maximum element of list", nums2, "is", maxNum2)
   
    nums3 = [-5, -1, -4, -10, -6]
    maxNum3 = maximum(nums3)
    print("maximum element of list", nums3, "is", maxNum3)

if __name__ == '__main__':
   main()
   
