# read and extract data from Overheads

# Overheads : The program will find the highest overhead category and its value. 
# Convert the amount flagged from part a, b and c using the real time exchange rate from the API call.

from pathlib import Path
import csv, requests, json, api

# iterate over the 3 csv files in the cvs_report folder
csvrep = Path.cwd()/"project_group"/"csv_reports"
for file in csvrep.glob("*.csv"):
    print(file)
overheads = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"


exp_list = []
with overheads.open(mode = 'r', encoding = 'UTF-8') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        exp_list.append(line)

# write data into txt file
file_path = Path.cwd()/"project_group"/"summary_report.txt"
print(file_path.exists())

#import exchange rate
exrate = api.apiwrite()

def high_heads():
    '''
    checks overheads and highlights the highest amount
    '''
    # the highest overhead will be highlighted in the summary report
    max_val = max(exp_list, key=lambda x: float(x[1]))
    rate = float(exrate)
    with file_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
        convert = (rate* float(max_val[1]))
        exp = (max_val[0]).upper()
        file.write(f"\n[HIGHEST OVERHEADS] {exp}: SGD {round(convert,2)}")

print(high_heads())
