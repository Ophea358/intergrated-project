# read and extract data from cash on hand

# Cash On Hand :  The program will compute the difference in Cash-on-Hand between each day. If Cash-on-Hand is not consecutively higher each day, the program will highlight the day where Cash-on-Hand is lower than the previous day and the value difference.
# Convert the amount flagged from part a, b and c using the real time exchange rate from the API call.

# import Path function from pathlib
from pathlib import Path
# import re, csv module
import csv, api

# csv file in the csv_report folder
csvrep = Path.cwd()/"project_group"/"csv_reports"
for file in csvrep.glob("*.csv"):
    print(file)
cash_on_hand = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"


# input data into list
cash_list = []
with cash_on_hand.open(mode = 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
        cash_list.append(line)
print(cash_list)

# write data into txt file
file_path = Path.cwd()/"project_group"/"summary_report.txt"
file_path.touch()
print(file_path)
print(file_path.exists())

# x is a placeholder
# day 83, 86 and 90 shld be flagged

# og numbers will be x
# i need to figure out a way to calc the diff between values, that will be y

def cash_def():
    '''
    calculates cash on hand and highlights deficits
    '''
    # any deficit figures will be put into deficit_list
    figure = cash_list(range(1,9))
    prev_figure = cash_list(range(8))
    deficit_list = []
    excrate = api.excrate()
    while True:
      if len(deficit_list) == 0:
          with file_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
              file.write(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
      else:
          # there are deficit values
          if figure < prev_figure:
              with file_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                  day = cash_list
                  convert = excrate* deficit_list
                  file.write(f"\n[CASH DEFICIT]DAY: {day}, AMOUNT: SGD {convert}")
          else:
              pass
print(cash_def())
