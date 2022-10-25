##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture7_class_exercises/groupby_GradeLevel.py
##name: Tong Yi
##email: ty680@hunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_info.csv")
#print(df)

grouped = df.groupby("Grade Level")
print("average grade by different grade level")
print(grouped['Score'].mean()) #show average grade for each grade level

seniorGroup = grouped.get_group("Senior")
print(seniorGroup['Score'].max()) #print max grade of senior students
