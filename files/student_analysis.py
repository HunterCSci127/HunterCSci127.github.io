##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture7_class_exercises/student_analysis.py
##name: Tong Yi
##email: ty680@hunter.cuny.edu
#Date: 2022-10-21 Fri 10:19 AM

#purpose: analyze student_info, which has Name, Age, Gender, Score, Grade Level
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("student_info.csv")
print("name info of students")
print(students["Name"])

print("Age info of students")
print(students["Age"])

print("score info of students")
print(students["Score"])

#Find out average grade of students and print it out
print("average grade of students")
print(students["Score"].mean())

print("max grade of students")
print(students["Score"].max())

print("min grade of students")
print(students["Score"].min())

grouped_gender = students.groupby("Gender")
#print(grouped_gender)
print(grouped_gender["Score"].mean())
print(grouped_gender.get_group('F')["Score"].mean())
