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

def find_coordinate():
    address = input("What is the location? -- :  ")
    arc = ArcGIS()
    location = arc.geocode(address)
    loc = "\nThis is the most closest location to your input \nIs this the right location?\n\n" + str(location) + "\n\nYes / No --:  "
    yn = input().lower()
    for columns in loc:
        print(columns, end="")
        t.sleep(0.7)
    if yn == "yes":
        latitude = location.latitude
        longitude = location.longitude
        return f"\nLatitude : {latitude}\nLongitude : {longitude}\n"
    elif yn == "no":
        find_coordinate()
    else:
        print("Wrong choice!\nTry Again!")
    


# Creating a function to load coordinates from an excel file
def find_bulk_coordinates():
    arc = ArcGIS()

    # Getting the file name
    file_name = input("What is the path of the file? -- :  ")

    # Checking if file exists or not
    if not os.path.exists(file_name):
        print("\nFile does not exist! \nCheck file path well!\n\n")

    else:
        # Opening and reading the file
        # with pd.read_excel(file_name, sheet_name=0) as df:

            # Gathering the necessary info for operation
            sheet_no = int(input("How many sheets are in the workbook? -- :  "))
            ps_name = input("What name have you stored the polling station names column? -- :  ")
            region = input("Which region are you dealing with? -- :  ")
            district = input("How have you stored the district column? -- :  ")


            # Giving a view of the file
            view = "Giving you a view of the file......\n\n"
            for columns in view:
                print(columns, end="")
                t.sleep(0.7)

            print(df[:5])


            # Putting up the conditions

            if sheet_no == 1:
                df = pd.read_excel(file_name, sheet_name=0)
            elif sheet_no > 1:
                worksheet = int(input("which sheet number has the locations to find the coordinates? -- :  "))
                df = pd.read_excel(file_name, sheet_name=worksheet-1)
            elif not int:
                print("Invalid input. \nInput must be an integer!")
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


while True:
    if user_choice == "1":
        print(find_coordinate())
        break

    elif user_choice == "2":
        find_bulk_coordinates()
        break

    else:
        print("Option not part of the given, Try again!")
        continue







