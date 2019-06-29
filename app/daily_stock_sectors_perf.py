# TO RUN THIS SCRIPT COPY THIS COMMAND INTO THE TERMINAL -----> daily_stock_sectors_perf.py

packages_setup = ['''

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

python daily_stock_sectors_perf.py

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


request_url = f"https://financialmodelingprep.com/api/v3/stock/sectors-performance"

response = requests.get(request_url)

# print(type(response))
# print(response.status_code)
# print(response.text) # This is a string

stock_sectors_parsed_response = json.loads(response.text) #this converts string format into dictionary

# print(crypto_list_parsed_response)

for i in stock_sectors_parsed_response["sectorPerformance"]:
    # print("Sector Name", i["sector"], "Change in %", i["changesPercentage"])

    daily_sector_name = i["sector"]
    daily_sector_pct_change = i["changesPercentage"]

    print("\n")
    print("Sector Name:")
    print(daily_sector_name)
    print("Change in %:", daily_sector_pct_change)

