##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture7_class_exercises/monthString2.py
##name: csci Teaching Staff

def monthString(month):
    monthNames = ['January', 'February', 'March', 'April',\
    'May', 'June', 'July', 'August', 'September',\
    'October', 'November', 'December']
    #\ means connect the next line
    #if you have codes spread more than one line,
    #you can use \ to connect these lines.
    
    if month < 1 or month > 12:
       return ""
    else:
       return monthNames[month-1]
       #if month == 1, return monthName[0],
       #if month == 2, return monthName[1],
       ...
       #if month == 12, return monthName[11].

def main():
    month = int(input("Enter a month in [1, 12]: "))
    #input("Enter a month in [1, 12]: ") takes input from user and
    #returns a string
    #int(input("Enter a month in [1, 12]: ")) returns an int

    print(monthString(month))

if __name__ == '__main__':
   main()

