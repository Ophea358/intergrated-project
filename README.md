# intergrated-project
collab repository for group project

# guide for pfb part

1.	Make an API call  to https://www.alphavantage.co to extract forex (FX) with the following API parameters:
•	function=FX_WEEKLY
•	from_symbol=USD 
•	to_symbol=SGD

Find the mean of the weekly closing forex price from the after extracting the forex as JSON data.


2.	Extract and summarise the data from the finance dashboard of the final round of business stimulation game from the MAB module. You can select to download the data from any day between day 40 to 50 of the game . The files should be downloaded in csv format. The automation will extract data from the following csv files:
3.	
a.	Profit & Loss :  Flag  the days and deficit amount of the net profit when the current day is lower than the previous day.
b.	Cash On Hand :  Flag the days and deficit amount when the current day is lower than the previous day.
c.	Overheads : Flag the  category with the highest overheads. 
d.	Convert the amount flagged from part a, b and c with the mean of the weekly closing forex price from the API call.

example for csv files in brief


# file structure
Folder : project_group
    │   main.py
    │   api.py
    │   read_file.py
    │   write_file.py
    │   deficit_report.txt
    │
    └─── Folder: csv_reports
               Cash on Hand.csv
               Overheads.csv
	      Profits and Loss.csv

# Modular Structure
Breaking a complex program into a modular structure often makes the program more manageable, easier to maintain and debug errors. 
When main.py is executed, it will:

•	Import the api.py  to make an API call to extract the required forex data and find the mean of the weekly closing price of the forex.
•	Import read_file.py will read the csv files Cash on Hand, Profit & Loss and Overheads from the csv_reports folder and extract the data needed for part 2a, 2b and 2c of the Automation Objectives.
•	Import write_file.py which will write the summarised data of Cash on Hand, Profit & Loss and Overheads to a text file: deficit.txt as shown in Figure 1.0
•	Refer to Figure 2.0 for the code contains in main.py as well as how the python files are structured in the group_project folder.


# Coding Skills

•	To complete the assignment successfully, use only the programming topics learned from PFB unless you are given the permission to do so. 
•	Use of external modules not taught will severely affect the marks. External module refers to additional module installed with pip install command.
•	However, you can use any built-in Python functions and modules not taught in PFB.

•	As this is a group project, you are required to collaborate with code into a GitHub repository. Each group member is expected to contribute and collaborate with GitHub. Besides the project objectives, each member will be graded based on their level of collaboration and contribution on GitHub. (contributions are visable)
