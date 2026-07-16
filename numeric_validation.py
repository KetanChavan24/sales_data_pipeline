import pandas as pd

file_path = "Europe_Sales_Records.csv"


data = pd.read_csv(file_path)

numeric_rules = {
    "pos" : ["Unit Price","Units Sold","Unit Cost"],
    "zero_pos" : ["Total Revenue","Total Cost"]
}


wrong_value_cols = {}
wrong_value_count = 0

for key in numeric_rules.keys():
    if(key == "pos"):
        for col in numeric_rules[key]:
            wrong_value_count  = (data[col] <= 0).sum()
            if(wrong_value_count):
                wrong_value_cols.update({col : wrong_value_count})
    elif(key == "zero_pos"):
        for col in numeric_rules[key]:
            wrong_value_count  = (data[col] < 0).sum()
            if(wrong_value_count ):
                wrong_value_cols.update({col : wrong_value_count})


if(wrong_value_cols):
    print("========== NUMERIC VALIDATION ==========")
    print("Invalid Numeric Values")
    for key,value in wrong_value_cols.items():
        print(f"{key} = {value}")
    print("Validation Status : FAILED")    
else:
    print("========== NUMERIC VALIDATION ==========")
    print("No numeric validation errors found.")
    print("Validation Status : PASSED")



        

