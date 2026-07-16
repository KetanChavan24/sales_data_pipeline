import pandas as pd
import sys

file_path = "Europe_Sales_Records.csv"

data = pd.read_csv(file_path)

mandat_columns = {
    "Region", "Country", "Order ID", "Order Date", "Ship Date", "Units Sold"
}


missing_values_cols = {}
for col in mandat_columns:
    individual_null_count_col = data[col].isnull().sum()
    if(individual_null_count_col):
        missing_values_cols.update({col: individual_null_count_col})
        

if(missing_values_cols):
    print("========== DATA VALIDATION ==========")
    print("Missing values found.")
    for key,value in missing_values_cols.items():
        print(f"{key}: {value}")
else:
    print("========== DATA VALIDATION ==========")
    print("No missing values found.")
    print("Validation Status : PASSED")






    
























#print(data.loc[3,"Region"])
# null_count = 0
# element = 0
# for col in mandat_columns:
#     while(element < len(data)):
#         if(data.loc[element,col] == 0):
#             null_count += 1

# missing_value_columns = {}
# for col in mandat_columns:
#     individual_col_count = data[col].isnull().sum()
#     col_w_null = col
#     if(individual_col_count):
        
        # if(null_count == 0):

# else:
#     print("========== DATA VALIDATION ==========")
#     print("Missing values:")
#     print("Validation Status : FAILED")






