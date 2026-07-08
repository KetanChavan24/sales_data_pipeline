import pandas as pd 
import sys


### EXTRACTION ###

file_path = "Europe_Sales_Records.csv"

try :
    data = pd.read_csv(file_path)
except pd.errors.EmptyDataError:
    print("The file is empty ")
    sys.exit(1)
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except pd.errors.ParserError:
    print("The file could not be parsed properly ")
    sys.exit(1)
except PermissionError:
    print("Permission denied while reading this file ")
    sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

print(data.columns.tolist())