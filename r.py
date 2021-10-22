from os import name
from typing import List
import folium
from numpy import longcomplex
import pandas

data = pandas.read_csv("C:/milo/vscode_milo/pers/Coo.txt")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
pop = list(data["POP"])

map = folium.Map(location=[28.679079, 77.069710], zoom_start=4, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="r map")

for lt, ln, pp in zip(lat, lon, pop):
    for i in pop:
        fg.add_child(folium.CircleMarker(location=(lt,ln), radius=8, fill_color='red', color='black', popup=str(i), fill=True, fill_opacity=1))

map.add_child(fg)

map.save("HEHE.html")