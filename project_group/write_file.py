# write data into txt file

from pathlib import Path

file_path = Path.cwd()/"project_group"
print(file_path)

import re, csv

empty_list = []

for file in file_path.glob("Cash on Hand.csv"):
    with file.open(mode = "r", encoding = 'UTF-8') as file:
        target = file.read()
    
