# read and extract data from Overheads

# Overheads : The program will find the highest overhead category and its value. 
# Convert the amount flagged from part a, b and c using the real time exchange rate from the API call.

from pathlib import Path
import csv, requests, json

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

def high_heads():
    '''
    checks overheads and highlights the highest amount
    '''
    # exchange rate data
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=GJVFL0NV2F7LZ8UV"
    response = requests.get(url)
    data = response.text
    # convert data to json to retrieve exchange rate  
    datadict = json.loads(data)
    dataval = datadict["Realtime Currency Exchange Rate"]
    exrate = dataval.get("5. Exchange Rate")

    # the highest overhead will be highlighted in the summary report
    figure = 0
    while figure <= len(exp_list):
        nested = exp_list[figure]
        max_val = 0
        nestval = float(nested[1])
        if nestval > max_val:
                max_val = nestval
                exp = nested[0]
        else:
            pass

    rate = float(exrate)
    with file_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                convert = (rate* max_val)
                exp = exp.touppercase()
                file.write(f"\n[HIGHEST OVERHEADS] {exp}: SGD {round(convert,2)}")
print(high_heads())
                
              
