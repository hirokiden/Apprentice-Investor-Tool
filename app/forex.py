# TO RUN THIS SCRIPT COPY THIS COMMAND INTO THE TERMINAL -----> forex.py

packages_setup = ['''

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

python forex.py

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


forex_request_url = f"https://financialmodelingprep.com/api/v3/forex"

forex_response = requests.get(forex_request_url)

# print(type(response))
# print(response.status_code)
# print(response.text) # This is a string

forex_parsed_response = json.loads(forex_response.text) #this converts string format into dictionary

# print(forex_parsed_response)

print("The following list contains a comprehensive daily snapshot of major currencies' Forex:")

for i in forex_parsed_response["forexList"]:
    # print(["ticker"],["bid"],["ask"],["open"],["low"],["high"],["changes"],["date"])
    # print(i["ticker"],i["bid"],i["ask"],i["open"],i["low"],i["high"],i["changes"],i["date"])

    forex_ticker = i["ticker"]
    forex_bid = i["bid"]
    forex_ask = i["ask"]
    forex_open = i["open"]
    forex_low = i["low"]
    forex_high = i["high"]
    forex_changes = i["changes"]
    forex_date = i["date"]


    print("\n")
    print("Forex Tickers:", forex_ticker)
    print("Forex Bid:", forex_bid)
    print("Forex Ask:", forex_ask)
    print("Forex Open:", forex_open)
    print("Forex Low:", forex_low)
    print("Forex High", forex_high)
    print("Forex Change:", forex_changes)
    print("Forex Date:", forex_date)
