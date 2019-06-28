# TO RUN THIS SCRIPT COPY THIS COMMAND INTO THE TERMINAL -----> market_open_close.py

packages_setup = ['''

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

python market_open_close.py

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


request_url = f"https://financialmodelingprep.com/api/v3/is-the-market-open"

response = requests.get(request_url)

# print(type(response))
# print(response.status_code)
# print(response.text) # This is a string

market_open_close_parsed_response = json.loads(response.text) #this converts string format into dictionary

# print(market_open_close_parsed_response)

# breakpoint()


if market_open_close_parsed_response["isTheStockMarketOpen"] == "True":
    open_or_not = "Open"
else:
    open_or_not = "Closed" 

this_calendar_year = market_open_close_parsed_response["stockMarketHolidays"][0]

# print("\n")
print("The", market_open_close_parsed_response["stockExchangeName"], "opens at", market_open_close_parsed_response["stockMarketHours"]["openingHour"], "and closes at", market_open_close_parsed_response["stockMarketHours"]["closingHour"], "on weekdays.")
print("\n")
print("The Stock Market is currently", open_or_not,".")
# print("\n")
print("Note that these are the upcoming holidays for the current Calendar Year:", this_calendar_year["year"])



# for i in market_open_close_parsed_response["stockMarketHolidays"]:

# Wanted to keep loop but the subsequent calendar year .json data is incorrect and will import only the top position [0]
    
# print("\n")
# print(this_calendar_year["year"], "Calendar year")
print("\n")
print(this_calendar_year["New Years Day"], "New Years Day")
print(this_calendar_year["Martin Luther King, Jr. Day"], "Martin Luther King, Jr. Day")
print(this_calendar_year["Washington's Birthday"], "Washington's Birthday")
print(this_calendar_year["Good Friday"], "Good Friday")
print(this_calendar_year["Memorial Day"], "Memorial Day")
print(this_calendar_year["Independence Day"], "Independence Day")
print(this_calendar_year["Labor Day"], "Labor Day")
print(this_calendar_year["Thanksgiving Day"], "Thanksgiving Day")
print(this_calendar_year["Christmas"], "Christmas")



# Reference Code Below -->

# or i in forex_parsed_response["forexList"]:
#     # print(["ticker"],["bid"],["ask"],["open"],["low"],["high"],["changes"],["date"])
#     print(i["ticker"],i["bid"],i["ask"],i["open"],i["low"],i["high"],i["changes"],i["date"])

# for k in most_gainer_parsed_response.keys():
#     ticker = most_gainer_parsed_response[k]
#     print(ticker["mostGainerStock"][""])

