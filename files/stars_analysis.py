##File name: /Users/laptopuser/Documents/courses/cs127/class_exercises/f22/lecture6_class_exercises/stars_analysis.py
##name: csci Teaching Staff

import pandas as pd

stars = pd.read_csv("stars.csv")

#Prints the luminosity of the brightest star.
print(stars['Luminosity(L/Lo)'].max())

#Prints the temperature of the coldest star.
print(stars['Temperature(K)'].min())

#Prints the average radius of a Hypergiant.
grouped = stars.groupby('Star type')
hypergiant = grouped.get_group('Hypergiant')
print("Hypergiant average radius:", hypergiant['Radius(R/Ro)'].mean())
print(stars.groupby('Star type').get_group('Hypergiant')['Radius(R/Ro)'].mean()) #also works, combine the groupby and get_group function 
#print(stars.groupby('Star type').mean()['Radius(R/Ro)'].max()) #also works, using the fact that hypergiant has the maximum average radius
#print(stars.groupby('Star type').get_group('Hypergiant').mean()['Radius(R/Ro)']) #also works, but deprecated
print("Hypergiant max radius:", hypergiant['Radius(R/Ro)'].max())
print(stars.groupby('Star type').max()['Radius(R/Ro)'].max())
