from pathlib import Path
import requests, json, os, re, csv

def api():
    '''
    retrieve real time exchange rate from the web
    '''
    # import forex exchange data  
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=GJVFL0NV2F7LZ8UV"
    response = requests.get(url)
    data = response.text
    print(data)
    # convert data to json to retrieve exchange rate
    data_info = json.loads(data)
    datakey  = data_info["Realtime Currency Exchange Rate"]
    exrate = datakey.get('5. Exchange Rate')
    
    # input real time currency conversion rate into summary report
    file_path = Path.cwd()/"project_group"/"summary_report.txt"
    with file_path.open(mode = "w") as file:
        file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{exrate}")

print(api())
