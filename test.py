import pandas as pd
from geopy.geocoders import ArcGIS


# Creating a function to load coordinates from an excel file
arc = ArcGIS()


df = pd.read_excel("Accra_2020.xlsx", sheet_name=0)
df["Address"] = df["PS Name"] + " " + df["District"] + " " + df["Region"]
df["Location"] = df["Location"].apply(arc.geocode)
df["Latitude"] = df["Location"].apply(lambda x : x.latitude if x != None else None)
df["Longitude"] = df["Location"].apply(lambda x : x.longitude if x != None else None)

df.to_excel("trial_test_done.xlsx", sheet_name="code test")