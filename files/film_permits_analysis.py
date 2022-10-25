##name: CS 127 teaching staff 
#file File_Permits.csv is downloaded from https://data.cityofnewyork.us/City-Government/Film-Permits/tg4x-b46p.
#Choose export and click CSV button.

#column names for Film_Permit.csv
#EventID,EventType,StartDateTime,EndDateTime,EnteredOn,EventAgency,ParkingHeld,Borough,CommunityBoard(s),PolicePrecinct(s),Category,SubCategoryName,Country,ZipCode(s)

import pandas as pd
import matplotlib.pyplot as plt

films = pd.read_csv("Film_Permits.csv")

#find out the ten most popular parking area for filming.
print(films['ParkingHeld'].value_counts()[:10])
#value_counts is a method, applied to a column,
#find out the frequencies (number of appearances)
#of its values, in descending order.

#find out the three most popular boroughs for filming. 
print(films['Borough'].value_counts()[:3])
