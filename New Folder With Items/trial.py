import pandas as pd
from geopy.geocoders import ArcGIS


# Creating a function to load coordinates from an excel file
arc = ArcGIS()


df1 = pd.read_excel("Accra_2020.xlsx", sheet_name=0)
df2 = pd.read_excel("Accra_2020.xlsx", sheet_name=1)
df3 = pd.read_excel("Accra_2020.xlsx", sheet_name=2)
df4 = pd.read_excel("Accra_2020.xlsx", sheet_name=3)
df5 = pd.read_excel("Accra_2020.xlsx", sheet_name=4)


df5["Address"] = df5["PS Name"] + " " + df5["District"] + " " + df5["Region"]
df5["Location"] = df5["Address"].apply(arc.geocode)
df5["Latitude"] = df5["Location"].apply(lambda x : x.latitude if x != None else None)
df5["Longitude"] = df5["Location"].apply(lambda x : x.longitude if x != None else None)

df5.to_excel("trial_test_done5000.xlsx", sheet_name="code test")