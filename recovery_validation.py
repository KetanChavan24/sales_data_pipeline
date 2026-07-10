import pandas as pd
import sys

file_path = "Europe_Sales_Records.csv"

data = pd.read_csv(file_path)

mandat_columns = {
    "Region", "Country", "Order ID", "Order Date", "Ship Date", "Units Sold"
}

#print(data.loc[3,"Region"])
# null_count = 0
# element = 0
# for col in mandat_columns:
#     while(element < len(data)):
#         if(data.loc[element,col] == 0):
#             null_count += 1


for col in mandat_columns:
    individual_col_count = data[col].isnull().sum()
    col_w_null = col
    if(individual_col_count):
        
        





if(null_count == 0):
    print("========== DATA VALIDATION ==========")
    print("No missing values found.")
    print("Validation Status : PASSED")
else:
    print("========== DATA VALIDATION ==========")
    print("Missing values:")
    print("Validation Status : FAILED")






