# write data into txt file

from pathlib import Path
import re,csv

file_path = Path.cwd()/"project_group"/"summary_report.txt"
file_path.touch()
print(file_path)
print(file_path.exists())

with file_path.open(mode = "w", encoding = "UTF-8", newline = "") as file:
  writer = csv.writer(file)
  writer.writerow([])
  writer.writerows( )
