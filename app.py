import pandas as pd  
from geopy.geocoders import ArcGIS
import graphics, time as t, os
from os import system as sys

# TODO 1 create a UI app for it using tkinter, kivy
# TODO 2 if doing for a specific region, define the upper and lower boundary limits of the longs and lats so as to not pick coordinates from those outside the defined boundaries.


# printing the logo

print(sys("clear"))

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
    loc = "\nThis is the location found per your input. \n\n\t\t__ " + str(location) +" __" + "\n\nIs this the right location? Yes / No --:  "
    
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
        print("\nWrong choice!\nTry Again!\n")
        

    


# Creating a function to load coordinates from an excel file
def find_bulk_coordinates():
    print(graphics.logo)

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
        # TODO 4 write an input to ask of how many columns exists in the file and change the codes to match the number of columns the user wants to add. 

        # Giving a view of the file
        sys("clear")
        print(graphics.logo)

        view = "Giving you a view of the file......\n\n"
        for columns in view:
            print(columns, end="")
            t.sleep(0.05)

        print(df.head(5))

        loading = "\n\nWorking on the file.\nIf the file has numerous rows it may take a while \nso relax and wait or you can continue with your other works and check later!\n\n"
        for columns in loading:
            print(columns, end="")
            t.sleep(0.05)

        df["address"] = df[ps_name] + " " + df[district] + " " + region
        df["location"] = df["address"].apply(arc.geocode)
        df["Latitude"] = df["location"].apply(lambda x : x.latitude if x != None else None)
        df["Longitude"] = df["location"].apply(lambda x : x.longitude if x != None else None)

        book_name = input("What name should the file be stored with? --:  ")
        sheet_name = input("\n\nWhat name should be given to the sheet? --:  ")
        
        df.to_excel(f"{book_name}.xlsx", sheet_name=sheet_name)

        print("\n\nFile successfully created!\nCheck your directory for the output!\n\n")






# The opening Message for user to make a choice on what they want to do

user_choice = input("""
Do you want to check for a single location or upload an excel file? :  

    1. Single location
    2. Upload an Excel file

--- :   """)


while True:
    
    if user_choice == "1":

        sys("clear")

        message = """

    .....................................................................................

                                \u26A0 NOTE BEFORE:

        To get the right location and coordinate or to enchance its accuracy,
        It is best you provide all the neccessary information you may have concerning
        the location you want.

        For example:
        { Region, District, Country, City, Zip - if foreign }
        
    .....................................................................................


    \n"""

        for columns in message:
            print(columns, end="")
            t.sleep(0.01)

        cont = input("Press Enter to continue...:  ")
        
        sys("clear")

        print(find_coordinate())
        break

    elif user_choice == "2":

        sys("clear")


        message = """

    .....................................................................................

                                \u26A0 NOTE BEFORE:

        This code was written with a specific file sample arrangemet in mind.
        Hence the columns align to that of the file and that is what is used.
        Changes will be made to make it better to work with different arrangements.

        If the columns are more than 1000rows, It is best suggested to break them 
        into files of 1000rows or any fit but below 1000 to avoid the API from breaking as
        limitations get put on it when run multiple times continually.

        Future updates will be made to cover such files and codes will be written to break
        them up and arrange them.

                                       IMPORTANT!

        Make sure you check column names well!
        If it gives you an error of { no column named "__input-column-name_" }, 
        check the excel file well you might have added a space after typing the name or before 
        it. Best to clear and retype it.

        Also, for files with first rows as a general heading, it is best to delete that row
        and let the file start with the column names.

        If it has more rows, it will take significant amount of time to complete the
        process. So you can run at the back and continue with your work.
        
    .....................................................................................

        \n"""

        for columns in message:
            print(columns, end="")
            t.sleep(0.01)

        cont = input("Press Enter to continue...:  ")

        sys("clear")

        find_bulk_coordinates()
        break

    else:
        print("\n\nOption not part of the given, Try again!\n\n")
        break
        







