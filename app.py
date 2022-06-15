import pandas as pd  
from geopy.geocoders import ArcGIS
import graphics 
import os, sys, time as t

# printing the logo

logo = graphics.logo
for columns in logo:
    print(columns, end='')
    t.sleep(0.003)


# Creating a function to load just a single coordinate

def find_coordinate(address_name):
    arc = ArcGIS()
    location = arc.geocode(address_name)
    print("\n" + str(location) + "\n")
    latitude = location.latitude
    longitude = location.longitude
    return f"Latitude : {latitude}\nLongitude : {longitude}\n"


# Creating a function to load coordinates from an excel file
def find_bulk_coordinates():
    arc = ArcGIS()

    # Opening and reading the file
    file_name = input("What is the path of the file? -- :  ")
    with pd.read_excel(file_name, sheet_name=0) as df:
        if not os.path.exists(file_name):
            print("File does not exist!")


    # Gathering the necessary info for operation
    
    sheet_no = int(input("How many sheets are in the workbook? -- :  "))
    ps_name = input("What name have you stored the polling station names column? -- :  ")
    # region = input("Which region are you dealing with? -- :  ")
    district = input("How have you stored the district column? -- :  ")

    # Putting up the conditions

    if not os.path.exists:
        print("File does not exist!")

    if sheet_no == 1:
        df = pd.read_excel(file_name, sheet_name=0)
    elif sheet_no > 1:
        worksheet = int(input("which sheet number has the locations to find the coordinates? -- :  "))
        df = pd.read_excel(file_name, sheet_name=worksheet-1)
    else:
        print("Workbook empty, Provide worksheet to work on!")
        quit()

    print(df)

    df["address"] = df[ps_name] + " " + df[district]
    df["location"] = df["address"].apply(arc.geocode)
    df["Latitude"] = df["location"].apply(lambda x : x.latitude if x != None else None)
    df["Longitude"] = df["location"].apply(lambda x : x.longitude if x != None else None)
    
    df.to_excel("trial_test_done.xlsx", sheet_name="code test")





# The opening Message for user to make a choice on what they want to do

user_choice = input("""
Do you want to check for a single location or upload an excel file? :  
1. Single location
2. Upload an Excel file

--- :   """)


if user_choice == "1":
    address = input("What is the location? -- :  ")
    print(find_coordinate(address))

elif user_choice == "2":
    find_bulk_coordinates()

else:
    print("Option not part of the given, Try again!")








