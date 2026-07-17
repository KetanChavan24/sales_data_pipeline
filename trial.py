import pandas as pd 
import sys


### EXTRACTION ###

file_path = "Europe_Sales_Records.csv"


data = pd.read_csv(file_path)

# print(data["Sales Channel"].unique())
# print(data["Order Priority"].unique())

help(pd.to_datetime)
