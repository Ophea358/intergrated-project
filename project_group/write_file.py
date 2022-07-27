# write data into txt file

from pathlib import Path

file_path = Path.cwd()/"project_group"
print(file_path)

with file_path.open(mode = "w", encoding = "UTF-8", newline = "
