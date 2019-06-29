# TO RUN THIS SCRIPT COPY THIS COMMAND INTO THE TERMINAL -----> crypto_ticker.py

packages_setup = ['''

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

python crypto_ticker.py

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

print("Please enter your desired crypto ticker")

bitcoin_ticker = input()

bitcoin_ticker_lower= bitcoin_ticker.lower()

crypto_list_request_url = f"https://financialmodelingprep.com/api/v3/cryptocurrency/{bitcoin_ticker_lower}"

crypto_list_parsed_response = requests.get(crypto_list_request_url)


# print(type(response))
# print(response.status_code)
# print(response.text) # This is a string

crypto_list_parsed_response = json.loads(crypto_list_parsed_response.text) #this converts string format into dictionary

try: 
    crypto_list_parsed_response["ticker"]
except:
    print("Please rerun the script and enter a valid crypto currency ticker")
    exit()

# print(crypto_parsed_response)


selected_crypo_ticker = crypto_list_parsed_response["ticker"]
selected_crypo_name = crypto_list_parsed_response[ "name"]
selected_crypo_price = crypto_list_parsed_response[ "price"]
selected_crypo_change = crypto_list_parsed_response[ "changes"]
selected_crypo_market_cap = crypto_list_parsed_response[ "marketCapitalization"]

# last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
# most_recent_open = parsed_response["Time Series (Daily)"][current_date]["1. open"]
# most_recent_close = parsed_response["Time Series (Daily)"][current_date]["4. close"]
# most_recent_high = parsed_response["Time Series (Daily)"][current_date]["2. high"]
# most_recent_low = parsed_response["Time Series (Daily)"][current_date]["3. low"]
# most_recent_total_volumes_traded = parsed_response["Time Series (Daily)"][current_date]["5. volume"]

print("The following list contains a snapshot of your chosen cryptocurrency's performance:")


print("Cryptocurrency Ticker:", selected_crypo_ticker)
print("Cryptocurrency Name:", selected_crypo_name)
print("Current Price: $", float(selected_crypo_price) ) 
print("Price Change:", usd_format( float(selected_crypo_change) ) )
print("Market Capitalization:", usd_format( float(selected_crypo_market_cap) ) )
