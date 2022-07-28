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
#file_path = Path.cwd()/"project_group"
#for file in file_path.glob('.csv'):
  #with open(file,mode='r',encoding='UTF-8') as files:
    #info=files.read()

# iterate over the 3 csv files in the cvs_report folder
for file in file_path.glob("*.csv"):
    print(file)

# csv files in the csv_report folder
overheads = file_path/"csv"/"Overheads.csv"

def data_collection(data):
  with data.open(mode = 'r', encoding = 'UTF-8') as files:
          info = files.read()
          overheads = re.findall(pattern = r"[E][X][P][E][N][S][E]", string = info)
          
          overheads = overheads.group

          file_path = Path.cwd()/"project_group"/"summary_report.txt"
          file_path_csv.exists()

          full_list = []
          with.open(r""
