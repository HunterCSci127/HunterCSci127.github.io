##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture10_class_exercises/getYear.py
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

def getYear():
    num = 0 #initialize num
    #Repeat entering num until it is in
    #(2000, 2021), neither end is included.
    #...invalid...(--valid input--)...invalid...
    #            2000           2021
    while num <= 2000 or num >= 2021:
        num = int(input("Enter a number after 2000 and before 2021: "))

    return num

def main():
    #variable num in function main() has nothing to do with
    #variable num in function getYear().
    num = getYear()
    print("The year is", num)

if __name__ == '__main__':
   main()
