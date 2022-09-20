##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture4_class_exercises/grade.py
##name: CSci 127 teaching staff 

#float is a number with decimal parts
grade = float(input("Enter your grade: "))

letter_grade = ' '
#peel onion from outermost layer, move towards inner layers,
#one layer a time.
if grade >= 90:
   letter_grade = 'A'
elif grade >= 80:
     letter_grade = 'B'
elif grade >= 70:
     letter_grade = 'C'
elif grade >= 60:
     letter_grade = 'D'
else:
     letter_grade = 'F'

print(letter_grade)
