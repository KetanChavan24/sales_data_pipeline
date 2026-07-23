import pandas as pd

file_path = "Europe_Sales_Records.csv"

data = pd.read_csv(file_path)

#CONSIDER THAT THE DATE VALUES ARE ALREADY VALIDATED AND HENCE WE ARE CONVERTING IT AGAIN IN DATETIME JUST FOR THE SAKE

date_cols = ["Order Date" , "Ship Date"]
str_to_date_data = pd.DataFrame()


for col in date_cols:   
    str_to_date_data[col] = pd.to_datetime(data[col], errors="coerce")

# for col in date_cols:  
#     str_to_date_data[col] = pd.to_datetime(data[col] , errors="coerce") 

invalid_rows = str_to_date_data[str_to_date_data["Ship Date"] < str_to_date_data["Order Date"]]
wrong_row_count = (str_to_date_data["Ship Date"] < str_to_date_data["Order Date"]).sum()

if(wrong_row_count):
    print("==========================================\n CROSS COLUMN VALIDATION \n ==========================================")
    print("Rule : Ship date >= Order date")
    print("Status : Failed")
    print(f"Total Invalid Rows : {wrong_row_count}")
    print(f"Rows affected : \n{invalid_rows}\n")
else:
    print("==========================================\n CROSS COLUMN VALIDATION \n ==========================================")
    print("Rule : Ship date >= Order date")
    print("Status : Success!")
  



# print(invalid_rows)