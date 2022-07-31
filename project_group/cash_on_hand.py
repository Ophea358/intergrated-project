# read and extract data from cash on hand

# Cash On Hand :  The program will compute the difference in Cash-on-Hand between each day. If Cash-on-Hand is not consecutively higher each day, the program will highlight the day where Cash-on-Hand is lower than the previous day and the value difference.
# Convert the amount flagged from part a, b and c using the real time exchange rate from the API call.

from pathlib import Path
import csv, requests, json

# csv file in the csv_report folder
csvrep = Path.cwd()/"project_group"/"csv_reports"
for file in csvrep.glob("*.csv"):
    print(file)
cash_on_hand = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"


# input data into list
cash_list = []
with cash_on_hand.open(mode = 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        print(line)
        cash_list.append(line)
print(cash_list)

# write data into txt file
file_path = Path.cwd()/"project_group"/"summary_report.txt"
print(file_path)
print(file_path.exists())

deficit_list = []

def cash_def():
    '''
    checks cash on hand and highlights deficits
    '''
    # exchange rate data
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=GJVFL0NV2F7LZ8UV"
    response = requests.get(url)
    data = response.text
    # convert data to json to retrieve exchange rate  
    datadict = json.loads(data)
    dataval = datadict["Realtime Currency Exchange Rate"]
    exrate = dataval.get("5. Exchange Rate")

    # any deficit figures will be put into deficit_list
    figure = 1
    prev_figure = 0
    while figure < len(cash_list):
        nested = cash_list[figure]
        prev_nested = cash_list[prev_figure]
        rate = float(exrate)
        if nested[1] < prev_nested[1]:
            for line in nested[1]:
                deficit_list.append(line)
            with file_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                day = float(nested[0])
                convert = (rate* float(nested[1]))
                file.write(f"\n[CASH DEFICIT]DAY: {day}, AMOUNT: SGD {round(convert,2)}")
                figure = figure + 1
                prev_figure = prev_figure + 1
        else:
            figure = figure + 1
            prev_figure = prev_figure + 1

        
print(cash_def())

def cash_sur():
    '''
    checks if there is a cash surplus
    '''
    if len(deficit_list) == 0:
        with file_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
            file.write(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    else:
        pass
print(cash_sur())
