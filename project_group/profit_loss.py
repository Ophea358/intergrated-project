# read and extract data from cash on hand

# Cash On Hand :  The program will compute the difference in the net profit between each day. If the net profit is not consecutively higher each day, the program will highlight the day where net profit is lower than the previous day and the value difference.
# Convert the amount flagged from part a, b and c using the real time exchange rate from the API call.

from pathlib import Path
import csv, requests, json, api

# csv file in the csv_report folder
csvrep = Path.cwd()/"project_group"/"csv_reports"
profit_loss = Path.cwd()/"project_group"/"csv_reports"/"Profit and Loss.csv"


# input data into list
net_list = []
with profit_loss.open(mode = 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        net_list.append(line)

# write data into txt file
file_path = Path.cwd()/"project_group"/"summary_report.txt"
print(file_path)
print(file_path.exists())

deficit_list = []
#import exchange rate
exrate = api.apiwrite()

def net_def():
    '''
    checks profit and loss and highlights deficits
    '''
    # any deficit figures will be highlighted in the summary report
    figure = 1
    prev_figure = 0
    while figure < len(net_list):
        nested = net_list[figure]
        prev_nested = net_list[prev_figure]
        rate = float(exrate)
        if nested[4] < prev_nested[4]:
            for line in nested[4]:
                deficit_list.append(line)
            with file_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                day = float(nested[0])
                convert = (rate* float(nested[1]))
                file.write(f"\n[NET PROFIT DEFICIT]DAY: {day}, AMOUNT: SGD {round(convert,2)}")
                figure = figure + 1
                prev_figure = prev_figure + 1
        else:
            figure = figure + 1
            prev_figure = prev_figure + 1

        
print(net_def())

def net_sur():
    '''
    checks if there is a net profit surplus
    '''
    if len(deficit_list) == 0:
        with file_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
            file.write(f"\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    else:
        pass
print(net_sur())
