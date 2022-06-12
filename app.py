import pandas as pd  
from geopy.geocoders import ArcGIS


# Creating a function to load just a single coordinate

def find_coordinate(address_name):
    arc = ArcGIS()
    location = arc.geocode(address_name)
    print(location)
    latitude = location.latitude
    longitude = location.longitude
    return f"Latitude : {latitude}\nLongitude : {longitude}\n"





address = input("What is the location? -- :  ")


print(find_coordinate(address))