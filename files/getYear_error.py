##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture10_class_exercises/getYear_error.py
##name: csci teaching staff 

#Write a function that asks a user for number after 2000 but 
#before 2021. The function should repeatedly ask the user for a number until
#they enter one within the range and return the number.

#sample input/output:
#Enter a number after 2000 and before 2021: 2022
#Enter a number after 2000 and before 2021: 2000
#Enter a number after 2000 and before 2021: 2021
#Enter a number after 2000 and before 2021: 2001
#The year you entered is 2001

num = 0
def getYear():
    #Repeat entering num until it is in (2000, 2021).
    #...invalid...(--valid input--)...invalid...
    #            2000           2021
    while num <= 2000 or num >= 2021:
        num = int(input("Enter a number after 2000 and before 2021: "))

    return num

def main():
    #num in main() has nothing to do with num in getYear().
    num = getYear()
    print("The year is", num)

if __name__ == '__main__':
   main()
