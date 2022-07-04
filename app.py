from aem import con
import pandas as pd  
from geopy.geocoders import ArcGIS
import graphics, time as t, os
from os import system as sys

# printing the logo

sys("clear")

logo = graphics.logo
for columns in logo:
    print(columns, end='')
    t.sleep(0.001)


# Creating a function to load just a single coordinate

def find_coordinate(): 
    print(graphics.logo)

    address = input("\nWhat is the location? -- :  ")
    arc = ArcGIS()
    location = arc.geocode(address)
    loc = "\nThis is the location found per your input. \n\n\t\t__" + str(location) +"__" + "\n\nIs this the right location? Yes / No --:  "
    
    for columns in loc:
        print(columns, end="")
        t.sleep(0.05)
    yn = input().lower()

    if yn == "yes":
        latitude = location.latitude
        longitude = location.longitude
        return f"\nLatitude : {latitude}\nLongitude : {longitude}\n"
    elif yn == "no":
        sys("clear")
        print(graphics.logo)
        print(find_coordinate())
    else:
        print("\nWrong choice!\nTry Again!")
    


# Creating a function to load coordinates from an excel file
def find_bulk_coordinates():

    # TODO 2 create a message to prompt on how to get accurate coordinate

    arc = ArcGIS()

    # Getting the file name
    file_name = input("\nWhat is the path of the file? -- :  ")

    # Checking if file exists or not
    if not os.path.exists(file_name):
        print("\nFile does not exist! \nCheck file path well and don't forget the file type extension (_.xlsx)!\n\n")

    else:
        # Opening and reading the file
        # with pd.read_excel(file_name, sheet_name=0) as df:

        # Gathering the necessary info for operation
        sheet_no = int(input("How many sheets are in the workbook? -- :  "))
        ps_name = input("What name have you stored the polling station names column? -- :  ")
        region = input("Which region are you dealing with? -- :  ")
        district = input("How have you stored the district column? -- :  ")


        # Putting up the conditions

        if sheet_no == 1:
            df = pd.read_excel(file_name, sheet_name=0)
        elif sheet_no > 1:
            worksheet = int(input("which sheet number has the locations to find the coordinates? -- :  "))
            df = pd.read_excel(file_name, sheet_name=worksheet-1)
        elif not int:
            print("Invalid input. \nInput must be an integer!")
            quit()
        else:
            print("Workbook empty, Provide worksheet to work on!")
            quit()

        # TODO 3 write conditions to check if column name does exist to prevent program from breaking

        # Giving a view of the file
        view = "Giving you a view of the file......\n\n"
        for columns in view:
            print(columns, end="")
            t.sleep(0.05)

        print(df[:5])

        loading = "Working on the file.\nIf the file has numerous rows it may take a while \nso relax and wait or you can continue with your other work and check later!\n\n"
        for columns in loading:
            print(columns, end="")

        df["address"] = df[ps_name] + " " + df[district] + " " + region
        df["location"] = df["address"].apply(arc.geocode)
        df["Latitude"] = df["location"].apply(lambda x : x.latitude if x != None else None)
        df["Longitude"] = df["location"].apply(lambda x : x.longitude if x != None else None)
        
        df.to_excel("trial_test_done.xlsx", sheet_name="code test")

        print("File successfully created!\nCheck your directory for the output!")






# The opening Message for user to make a choice on what they want to do

user_choice = input("""
Do you want to check for a single location or upload an excel file? :  
1. Single location
2. Upload an Excel file

--- :   """)


while True:
    
    if user_choice == "1":

        sys("clear")

        # TODO 1 create a message to prompt on how to get accurate coordinate
        message = """

    .....................................................................................

                                \u26A0 NOTE BEFORE:

        To get the right location and coordinate or to enchance its accuracy,
        It is best you provide all the neccessary information you may have concerning
        the location you want.

        For example:
        { Region, District, Country, City, Zip - if foreign }
        
    .....................................................................................


    Will skip to the next page in 15s....

        """

        for columns in message:
            print(columns, end="")
            t.sleep(0.02)
    
        wait_to_next = " "
        print(wait_to_next)
        t.sleep(15)
        sys("clear")

        print(find_coordinate())
        break

    elif user_choice == "2":
        find_bulk_coordinates()
        break

    else:
        print("\n\nOption not part of the given, Try again!\n\n")
        break
        







