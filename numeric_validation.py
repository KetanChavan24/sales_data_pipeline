import pandas as pd

file_path = "Europe_Sales_Records.csv"


data = pd.read_csv(file_path)

numeric_rules = {
    "pos" : ["unit price","Units Sold","Unit_cost"],
    "zero_pos" : ["Total Revenue","Total Cost"]
}


not_pos_col = 0
not_pos_cols = {}
not_zero_pos_col = 0
not_zero_pos_cols = {}

for key in numeric_rules.keys():
    if(key == "pos"):
        for col in numeric_rules.keys():
            not_pos_col = data[col] <= 0
            if(not_pos_col):
                not_pos_cols.update({col : not_pos_col})

    elif(key == "zero_pos"):
        for col in numeric_rules.keys():
            not_zero_pos_col = data[col] < 0
            if(not_zero_pos_col):
                not_zero_pos_cols.update({col : not_zero_pos_col})


if(not_pos_col):
    print("========== NUMERIC VALIDATION ==========")
    print("Invalid Numeric Values")
    for key,value in not_pos_cols.items():
        print(f"{key} = {value}")
    print("Validation Status : FAILED")    
elif(not_zero_pos_cols):
    print("========== NUMERIC VALIDATION ==========")
    print("Invalid Numeric Values")
    for key,value in not_zero_pos_cols.items():
        print(f"{key} = {value}")
    print("Validation Status : FAILED")    
else:
    print("========== NUMERIC VALIDATION ==========")
    print("No numeric validation errors found.")
    print("Validation Status : PASSED")



        

