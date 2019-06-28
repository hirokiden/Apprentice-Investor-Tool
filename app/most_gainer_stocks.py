# TO RUN THIS SCRIPT COPY THIS COMMAND INTO THE TERMINAL -----> most_gainer_stocks.py

packages_setup = ['''

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

python most_gainer_stocks.py

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


request_url = f"https://financialmodelingprep.com/api/v3/stock/gainers"

response = requests.get(request_url)

# print(type(response))
# print(response.status_code)
# print(response.text) # This is a string

most_gainer_parsed_response = json.loads(response.text) #this converts string format into dictionary

# print(most_gainer_parsed_response)

# breakpoint()

# print(most_gainer_parsed_response["mostGainerStock"]["ticker"][1])

for i in most_gainer_parsed_response["mostGainerStock"]:
    # print(i["ticker"], i["price"], i["changes"], i["changesPercentage"], i["companyName"])
    mgs_ticker = i["ticker"]
    mgs_price = i["price"]
    mgs_changes = i["changes"]
    mgs_company_name = i["companyName"]

    print("\n")
    print(mgs_ticker)
    print(mgs_company_name)
    print(mgs_price)
    print(mgs_changes)
    