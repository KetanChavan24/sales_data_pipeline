import pandas as pd

file_path = "Europe_Sales_Records.csv"

data = pd.read_csv(file_path)

mandat_unique_col = ["Order ID"]
duplicate_rows = {}


for col in mandat_unique_col:
    if((data[col].duplicated()).sum() > 0):
        duplicate_row_ind = data[data[col].duplicated()]
        duplicate_row_count = (data[col].duplicated()).sum()
        duplicate_rows.update({col : {"count" : duplicate_row_count , "rows" : duplicate_row_ind }})



if(duplicate_rows):
    print("========================================== Duplicate VALIDATION ==========================================")
    print("Duplicate values found!")
    for key,value in duplicate_rows.items():
        print(f"{key}: {value}")
    print("status : failed")
else:
    print("========================================== Duplicate VALIDATION ==========================================")
    print("No Duplicate values found!")
    print("status : Success!")


