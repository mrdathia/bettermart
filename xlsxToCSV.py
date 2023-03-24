# importe required libraries
import openpyxl
import csv
import pandas as pd

# open given workbook
# and store in Excel object
excel = openpyxl.load_workbook("filteredData.xlsx")

# select the active sheet
sheet = excel.active
# writer object is created
col = csv.writer(open("testData.csv",
                      'w', newline="\n"))

# writing the data in csv file
for r in sheet.rows:
    # row by row write
    # operation is performed
    col.writerow([cell.value for cell in r])

# read the csv file and
# convert into dataframe object
