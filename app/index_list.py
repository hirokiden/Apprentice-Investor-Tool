# TO RUN THIS SCRIPT COPY THIS COMMAND INTO THE TERMINAL -----> index_list.py

packages_setup = ['''

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

python index_list.py


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


request_url = f"https://financialmodelingprep.com/api/v3/majors-indexes"

response = requests.get(request_url)

# print(type(response))
# print(response.status_code)
# print(response.text) # This is a string

index_list_parsed_response = json.loads(response.text) #this converts string format into dictionary

# print(index_list_parsed_response)

# breakpoint()

# variable ="txt"
# print("{:^5s}".format(variable))
# print("{:^10s}".format(variable))
# print("{:^15s}".format(variable))
# print("{:^25s}".format(variable))
# print("{:^35s}".format(variable))
# print("{:^45s}".format(variable))
# print("{:^55s}".format(variable))
# print("{:^65s}".format(variable))
# print("{:^75s}".format(variable))

# def aligner1 (spacer):
#     return '{:>8}'.format(*str(spacer))

#     f"{'Trades:':<15}{cnt:>10}",

# "{:>20} {:>10} {:>10}".format(*cols)s
# def aligner2 (spacer):
#     return (str(spacer).rjust(20, '-'))

# def aligner3 (spacer):
#     return "{:^35s}".format(spacer)

# def aligner4 (spacer):
#     return "{:^45s}".format(spacer)

# def aligner4 (spacer):
#     return "{:^55s}".format(spacer)

# def aligner4 (spacer):
#     return "{:^65s}".format(spacer)

# print(aligner("tester"))

for i in index_list_parsed_response["majorIndexesList"]:
    print("\n")
    # print( i["ticker"], ",", i["indexName"], ",",  i["price"], ",",  i["changes"] )
    ticker = i["ticker"]
    index_name = i["indexName"]
    price = i["price"]
    changes = i["changes"]
    print(ticker)
    print (index_name)
    print( price)
    print(changes)

