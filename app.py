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




# Creating a function to load coordinates from an excel file
def find_bulk_coordinates():
    arc = ArcGIS()
    file_name = input("What is the path of the file? -- :  ")
    sheet_no = int(input("How many sheets are in the workbook? -- :  "))
    worksheet = int(input("which sheet number had the locations to find the coordinates? -- :  "))
    if 
    df = pd.read















address = input("What is the location? -- :  ")


print(find_coordinate(address))