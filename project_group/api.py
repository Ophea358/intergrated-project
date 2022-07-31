from pathlib import Path
import requests, json


def apiwrite():
    '''
    write real time exchange rate from the web into files
    '''
    # import forex exchange data  
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=GJVFL0NV2F7LZ8UV"
    response = requests.get(url)
    data = response.text
    # convert data to json to retrieve exchange rate  
    datadict = json.loads(data)
    dataval = datadict["Realtime Currency Exchange Rate"]
    exrate = dataval["5. Exchange Rate"]

    # input real time currency conversion rate into summary report
    file_path = Path.cwd()/"project_group"/"summary_report.txt"
    file_path.touch
    with file_path.open(mode = "w") as file:
        file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{exrate}")
print(apiwrite())
