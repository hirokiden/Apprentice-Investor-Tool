# app/company_profile.py

# modules
import json # to parse JSON
import csv # to export to CSV
import os # operating system dependent functionality
import datetime

# packages
from dotenv import load_dotenv
import requests


load_dotenv() # loads from .env

# function to convert numbers to USD
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

portfolio_option = 0
loop = 0
investor_portfolio = []
while loop == 0:

    # to create an equity portfolio
    print("\n")
    print("Apprentice Investor allows you to create, modify and track a portfolio of stocks!")
    print("Option 1: Add a ticker to the portfolio")
    print("Option 2: Remove a ticker from the portfolio")
    print("Option 3: View the portfolio")
    print("Option 4: Valuation analysis of your portfolio")
    print("Option 5: Time series analysis of your portfolio")
    print("Option 6: Return to the main screen")
    portfolio_option = input("Please type a number between 1 and 6:")
    portfolio_option = int(portfolio_option)    
    while portfolio_option > 6 or portfolio_option < 1:
        portfolio_option = input("Incorrect input.  Please type a number between 1 and 6:")
        portfolio_option = int(portfolio_option)
    
    test = False
    if portfolio_option == 1:
        symbol = input("Please enter ticker symbol")
        request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
        response = requests.get(request_url)
        parsed_response = json.loads(response.text)
        if len(symbol) > 5:
            symbol = input("Ticker invalid.  Please enter a new ticker: ")
            request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
            response = requests.get(request_url)
            parsed_response = json.loads(response.text) 
        elif 'Error' in parsed_response.keys():
            symbol = input("Ticker invalid.  Please enter a new ticker: ")
            request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
            response = requests.get(request_url)
            parsed_response = json.loads(response.text)
        else:
            investor_portfolio.append(symbol)
            print("Ticker added to portfolio")   
            
    
    