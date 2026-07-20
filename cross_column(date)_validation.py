import pandas as pd

file_path = "Europe_Sales_Records.csv"


data = pd.read_csv(file_path)

#CONSIDER THAT THE DATE VALUES ARE ALREADY VALIDATED AND HENCE WE ARE CONVERTING IT AGAIN IN DATETIME JUST FOR THE SAKE

date_cols = ["Order Date" , "Ship Date"]
str_to_date_data = pd.DataFrame()
wrong_rows = {}
wrong_row_count = 0

for col in date_cols:
    str_to_date_data[col] = pd.to_datetime(data[col], errors="coerce")
#print(str_to_date_data)

# for val in str_to_date_data:

# order_date = str_to_date_data["Order Date"]
# ship_date = str_to_date_data["Ship Date"]

# for odate in order_date:
#     for sdate in ship_date:
#         wrong_row_count = (data[])

for row in str_to_date_data:
    wrong_row_count = (data[data[]])


    



