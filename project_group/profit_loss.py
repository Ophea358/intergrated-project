# read and extract data from files

# flag = mark 
# deficit = when money is too small / an excess of expenditure or liabilities over income or assets in a given period

# Profit & Loss :  Flag  the days and deficit amount of the net profit when the current day is lower than the previous day.
# Cash On Hand :  Flag the days and deficit amount when the current day is lower than the previous day.
# Overheads : Flag the  category with the highest overheads. 
# Convert the amount flagged from part a, b and c with the mean of the weekly closing forex price from the API call.

# import Path function from pathlib
from pathlib import Path
# import re, csv module
import re, csv

# instantiate a file path object to current working directory
file_path = Path.cwd()/"project_group"
#for file in file_path.glob('.csv'):
  #with open(file,mode='r',encoding='UTF-8') as files:
    #info=files.read()

# iterate over the 3 csv files in the cvs_report folder
#for file in file_path.glob("*.csv"):
    #print(file)

# csv files in the csv_report folder
profit_loss = Path.cwd()/"project_group"/"csv_reports"/"Porift and Loss.csv"
  with profit_loss.open(mode = 'r', encoding = 'UTF-8') as file:
    target = file.read()
  for line in target:

  day = re.findall(pattern = "[0-9][0-9]", string = target)[0]
  sales = re.findall(pattern = r"[0-8].+", string = target)[0]
  trading_profit = re.findall(pattern = r"[0-8].+", string = target)[1]
  print(trading_profit)

def data_collection(data):
  with data.open(mode = 'r', encoding = 'UTF-8') as files:
    info = files.read()
  profit_loss = re.findall(pattern = r"", string = info)

# write data into txt file

from pathlib import Path
import re,csv

#ile_path = Path.cwd()/"project_group"/"summary_report.txt"
#file_path.touch()
#print(file_path)
#print(file_path.exists())

#with file_path.open(mode = "w", encoding = "UTF-8", newline = "") as file:
  #writer = csv.writer(file)
  #writer.writerow([])
  #writer.writerows( )
