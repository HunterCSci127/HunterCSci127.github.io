#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:17:29 2017

@author: stjohn
"""

import folium
#from folium.plugins import MarkerCluster
import pandas as pd
#import numpy as np


cuny = pd.read_csv('cunyLocations.csv')
print (cuny)
mapCUNY = folium.Map(location=[40.75, -74.125])

coords = []
popups = []

for index,row in cuny.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)

mapCUNY.save(outfile='cunyLocations.html')



