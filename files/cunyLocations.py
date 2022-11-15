import folium
import pandas as pd
import webbrowser #display html file
import os #use to find directory

#Use pandas (alias pd) to read a csv file,
#save the return data frame object in variable cuny.
cuny = pd.read_csv('cunyLocations.csv')

#Create a map object centered at 40.75, -74.125,
#save in variable mapCUNY.
mapCUNY = folium.Map(location = [40.75, -74.125])

for index, row in cuny.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    if row["College or Institution Type"] == "Senior Colleges":
       collegeIcon = folium.Icon(color="purple")
    else: collegeIcon = folium.Icon(color="blue")

    #create a marker, sepcify its latitude, longitude,
    #pop up name, and icon, save in variable newMarker.
    newMarker = folium.Marker([lat, lon], popup=name, icon=collegeIcon)
    newMarker.add_to(mapCUNY)

filename = 'cunyLocationsSenior.html'

#save mapCUNY to filename
mapCUNY.save(outfile = filename)

#display html using open method of webbrowser class
webbrowser.open('file://' + os.path.realpath(filename))
