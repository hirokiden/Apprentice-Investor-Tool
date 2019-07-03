#  python Testing.py



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


# api_key = "demo" --> no longer in use, API_KEY replaces the {demo} component of request_url later on

# print("Please enter a valid stock ticker symbol!  As an example, Disney is 'DIS' and AT&T is 'T'. ")


user_input_ticker = input()
# testuser_input_ticker = input()

# while True:
#     user_input_ticker = input()
#     # testuser_input_ticker = input()

#     if user_input_ticker.isdigit() == True: # Attributed this line of code concept to prior shopping cart usage 
#         # more details located from https://www.tutorialspoint.com/python/string_isdigit.htm, script concept borrowed from website after research
#         print("Ticker cannot be a number, please try again")
#     elif len(user_input_ticker) > 5:
#         print("Ticker cannot exceed 5 characters, please try again")
#     else:
#         break


batch_financial_statement_request_url = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{user_input_ticker}"

batch_financial_statement_response = requests.get(batch_financial_statement_request_url)

# print(type(response))
# print(response.status_code)
# print(response.text) # This is a string


batch_financial_statement_parsed_response = json.loads(batch_financial_statement_response.text) #this converts string format into dictionary

try: 
    batch_financial_statement_parsed_response["symbol"]
except:
    print("Invalid ticker, please rerun the script and try again")
    exit()

batch_financial_symbols = batch_financial_statement_parsed_response["symbol"]

batch_financial_list = batch_financial_statement_parsed_response["financials"]

# print(batch_financial_list)


list_of_financial_statement_dates = list(batch_financial_list) # convert the dates dictionary keys into list format

# print(list_of_financial_statement_dates)

print( list_of_financial_statement_dates[:500] )