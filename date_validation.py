import pandas as pd

file_path = "Europe_Sales_Records.csv"


data = pd.read_csv(file_path)

date_cols = ["Order Date" , "Ship Date"]
nat_edited_data = pd.DataFrame()

for col in date_cols:
    nat_edited_data[col] = pd.to_datetime(data[col], errors="coerce")

#counting
wrong_date_count = 0
wrong_date_cols = {}
for col in date_cols:
    wrong_date_count = nat_edited_data[col].isna().sum()
    if(wrong_date_count):
        wrong_date_cols.update({col : wrong_date_count})


if(wrong_date_cols):
    print("========== DATE VALIDATION ==========")
    print("INVALID DATES FOUND")
    for key, value in wrong_date_cols.items():
        print(f"{key}: {value}")
    print("Validation Status : FAILED")
else:
    print("========== DATE VALIDATION ==========")
    print("No invalid dates found.")
    print("Validation Status : PASSED")

    
