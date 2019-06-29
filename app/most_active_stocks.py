# python most_active_stocks.py

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


#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/api/stock/actives?datatype=json")
# print(get_jsonparsed_data(url))


most_active_parser_response = get_jsonparsed_data(url)


# print(most_active_parser_response)

# print(most_active_parser_response)


# breakpoint()


print("You are pulling this information at:", date_time)
print("The Most Active Stock Traded is:")

for k in most_active_parser_response.keys():
    ticker = most_active_parser_response[k]
    # print("Ticker Symbol: ", ticker["Ticker"], "Price: ", ticker["Price"], "$ Change: ", ticker["Changes"], "% Change: ", ticker["ChangesPerc"], "Company Name: ", ticker["companyName"])

    mas_ticker = ticker["Ticker"]
    mas_price = ticker["Price"]
    mas_change = ticker["Changes"]
    mas_change_pct = ticker["ChangesPerc"]
    mas_comp_name = ticker["companyName"]

    print("\n")
    print("Stock Ticker:", mas_ticker)
    print("Company Name:", mas_comp_name)
    print("Current Price:", usd_format( float(mas_price) ) )
    print("Price Change:", usd_format( float(mas_change) ) )
    print("Price Change %:", usd_format( float(mas_change_pct) ) )
    

# parameters for print 

# dataframe