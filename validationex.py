import pandas as pd 

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
print(set(data.columns))

