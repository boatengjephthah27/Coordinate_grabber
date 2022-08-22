import pandas as pd  
from geopy.geocoders import ArcGIS
import time as t, os
from os import system as sys





def find_bulk_coordinates():  

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
        # ps_name = input("What name have you stored the polling station names column? -- :  ")
        # region = input("Which region are you dealing with? -- :  ")
        # district = input("How have you stored the district column? -- :  ")


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

        view = "Giving you a view of the file......\n\n"
        for columns in view:
            print(columns, end="")
            t.sleep(0.05)

        print(df.head(5))

        loading = "\n\nWorking on the file.\nIf the file has numerous rows it may take a while \nso relax and wait or you can continue with your other works and check later!\n\n"
        for columns in loading:
            print(columns, end="")
            t.sleep(0.05)

        df["address"] = df["PS Name"] + " " + df["DISTRICT"]
        df["location"] = df["address"].apply(arc.geocode)
        df["Latitude"] = df["location"].apply(lambda x : x.latitude if x != None else None)
        df["Longitude"] = df["location"].apply(lambda x : x.longitude if x != None else None)

        book_name = input("What name should the file be stored with? --:  ")
        sheet_name = input("\n\nWhat name should be given to the sheet? --:  ")
        
        df.to_excel(f"{book_name}.xlsx", sheet_name=sheet_name)

        print("\n\nFile successfully created!\nCheck your directory for the output!\n\n")



find_bulk_coordinates()