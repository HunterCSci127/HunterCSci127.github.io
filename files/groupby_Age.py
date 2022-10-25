##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture7_class_exercises/groupby_Age.py
##name: Tong Yi
##email: ty680@hunter.cuny.edu
#Date: 2022-09-30 Fri 10:49 AM

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_info.csv")
#Name,Gender,Age,Grade Level,Score
#Ann C.,F,17,Freshman,88.5
#Bob S.,M,18,Sophomore,90.6
#Charles T.,M,22,Senior,82.6
#Deb O.,F,22,Senior,75
#Edward K.,M,18,Freshman,77
#Fred J.,M,19,Junior,92
#George L.,M,19,Junior,72
#Hillary L.,F,20,Sophomore,81

#df.plot(x='Name', y='Score')
#df.plot() #only display numerical data like age and score.
#plt.show() #needed, otherwise the figure specified in plot method of data frame object df is not shown.
grouped = df.groupby('Age')
#get average score by each group
print(grouped['Score'].mean())

age18 = grouped.get_group(18)
print(age18['Score'].max()) #max grade in group of age 18
