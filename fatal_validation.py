import pandas as pd
import sys

file_path = "Europe_Sales_Records.csv"

data = pd.read_csv(file_path)


#Expected columns
exp_columns = {
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Priority",
    "Order Date",
    "Order ID",
    "Ship Date",
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit"
}

#incoming schema
inc_columns = set(data.columns)

#missing_columns and expected_columns
missing_columns = exp_columns - inc_columns
unexpected_columns = inc_columns - exp_columns

if missing_columns or unexpected_columns:
    print("SCHEMA FAILED !")
    if missing_columns:
        print(f"missing columns: \n {missing_columns}")
    if unexpected_columns:
        print(f"unexpected columns: \n {unexpected_columns}")
    

    sys.exit(1)

#SCHEMA SUCCESS VALIDATION
else:
    print("SCHEMA SUCCESS!!")




