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

# iterate over the 3 csv files in the csv folder
for file in home.glob('.csv'):
profit_and_loss = file_path/"profit_and_loss.csv"
