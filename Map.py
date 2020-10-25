# Description: This program creates a map of the trains within the NYC Transit System based on data from
# NYC Open Data. Each station will have a heatmap, marker, station name, and track letter(s).
# The map is accessible through Jupyter with Map.ipynb

#Required Libraries: gmaps (includes Jupyter and other dependencies), pandas, requests

# Author: Moris Goldshtein
# Contributors: Neil Kuldip, Luna Shin




import requests
import gmaps
import pandas as pd

#Personal api key
API_KEY = "AIzaSyBLbuemf2HbOtD8JjWfS7E2q3uTTDGhIKw"

#Gain access to google's javascript api
gmaps.configure(api_key="AIzaSyBLbuemf2HbOtD8JjWfS7E2q3uTTDGhIKw")
new_york_coordinates = (40.69, -73.8073)






#Use pandas to access a csv containing info on train stations in Queens                                                                 
df = pd.read_csv('Subway_Stations.csv')                                                                 
stations = df['the_geom']                                                                   
list_of_coordinates = stations.values

#list to contain coordinates(in tuple form) of each train station
places = []

#The coordinates for each train station are in string form -> turn them into floats for the gmaps to use
for x in range(0, len(stations.values)):
    #Remove the "POINT " in every value, note each value is a string
    stations.values[x] = stations.values[x][7:-1]
    #Separate the two values(which are strings right now) by finding where the (space) is
    index = stations.values[x].find(" ")
    float1 = stations.values[x][index+1:]
    float2 = stations.values[x][:index]
    #Convert each value to a float and then recombine them into a tuple
    float1 = float(float1)
    float2 = float(float2)
    stations.values[x] = (float1, float2)
    #Add each value to places
    places.append(stations.values[x])




#Access same csv, but the names of each train station instead of coordinates
stations = df['NAME']
list_of_names = stations.values

#list to contain names of each train station
names = []

#Add every name to the list
for x in range(0, len(stations.values)):
    names.append(stations.values[x])




#Access same csv, but the lines of each train station instead of coordinates
stations = df['LINE']
list_of_lines = stations.values

#list to contain names of each train station
lines = []

#Add every name to the list
for x in range(0, len(stations.values)):
    lines.append(stations.values[x])








#Create the map
fig = gmaps.figure(center=new_york_coordinates, zoom_level=11.2, layout={'height': '700px', 'width': '700px'})

#Show all train lines
transit_layer = gmaps.transit_layer()
fig.add_layer(transit_layer)

#Make a heatmap area around every coordinate based on the modified info from the csv (The circle is ~1/4 mile based on set zoom level without zooming)
heat_map_layer = gmaps.heatmap_layer(locations=places, point_radius=11)
fig.add_layer(heat_map_layer)

#Make markers for every station so they can be identified by name
name_marker_layer = gmaps.marker_layer(
    places, info_box_content=names, hover_text=lines)

fig.add_layer(name_marker_layer)

#Activate the map
fig 
