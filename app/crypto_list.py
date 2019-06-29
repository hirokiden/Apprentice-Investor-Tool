# TO RUN THIS SCRIPT COPY THIS COMMAND INTO THE TERMINAL -----> crypto_list.py

packages_setup = ['''

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

python crypto_list.py

''']


# Examples (click for JSON output)
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo



# To issue an http request in python, you must import a 'request package'

import os
import requests
import json # need this to import json string into dictionary
from datetime import datetime # taken from stackoverflow
import csv # so you can write date to .csv


# Current Time for transaction pull
date_time = datetime.now().strftime("%m/%d/%Y, %I:%M:%S%P\n") # Formatted for easy to understand human reading instead of military time
# print(date_time)

# Also, we know that we are working with $ pricing so let's get the formatting out of the way

def usd_format(my_price):
    return "${0:,.2f}".format(my_price) # This UDF will change numerical denomination to currency and cents (2 digits) format when passed through


# request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={user_input_ticker}&apikey={api_key}"


request_url = f"https://financialmodelingprep.com/api/v3/cryptocurrencies"

response = requests.get(request_url)

# print(type(response))
# print(response.status_code)
# print(response.text) # This is a string

crypto_list_parsed_response = json.loads(response.text) #this converts string format into dictionary

# print(crypto_list_parsed_response)

print("The following list contains a comprehensive snapshot of major cryptocurrecies' performance:")

for i in crypto_list_parsed_response["cryptocurrenciesList"]:
    # print(i["ticker"], i["name"], i["price"], i["changes"], i["marketCapitalization"])
    c_list_ticker = i["ticker"]
    c_list_crypto_name = i["name"]
    c_list_price = i["price"]
    c_list_change = i["changes"]
    c_list_market_cap = i["marketCapitalization"]

    print("\n")
    print("Cryptocurrency Ticker:", c_list_ticker)
    print("Cryptocurrency Name:", c_list_crypto_name)
    print("Current Price:", usd_format( float(c_list_price) ) )
    print("Price Change:", usd_format( float(c_list_change) ) )
    print("Market Capitalization:", usd_format( float(c_list_market_cap) ) )







# selected_crypo_ticker = crypto_list_parsed_response["cryptocurrenciesList"][0]
# # selected_crypo_name = crypto_list_parsed_response[ "name"]
# # selected_crypo_price = crypto_list_parsed_response[ "price"]
# # selected_crypo_change = crypto_list_parsed_response[ "changes"]
# # selected_crypo_market_cap = crypto_list_parsed_response[ "marketCapitalization"]


# print(selected_crypo_ticker)
# # print(selected_crypo_name)
# # print(selected_crypo_price)
# print(selected_crypo_change)
# print(selected_crypo_market_cap)