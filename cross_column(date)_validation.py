import pandas as pd

file_path = "Europe_Sales_Records.csv"


data = pd.read_csv(file_path)

#CONSIDER THAT THE DATE VALUES ARE ALREADY VALIDATED AND HENCE WE ARE CONVERTING IT AGAIN IN DATETIME JUST FOR THE SAKE

date_cols = ["Order Date" , "Ship Date"]
str_to_date_data = pd.DataFrame()

for col in date_cols:
    str_to_date_data[col] = pd.to_datetime(data[col], errors="coerce")




