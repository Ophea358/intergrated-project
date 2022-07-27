# import forex exchange data and get mean weekly closing price 
import requests

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=GJVFL0NV2F7LZ8UV"
response = requests.get(url)
data = response.json()
print(data)
