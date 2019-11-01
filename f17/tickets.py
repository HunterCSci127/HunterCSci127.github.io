#CSci 127 Teaching Staff
#October 2017
#Count which cars got the most parking tickets

#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
print(tickets["Vehicle Year"].value_counts()[:10]) #Print out the dataframe
