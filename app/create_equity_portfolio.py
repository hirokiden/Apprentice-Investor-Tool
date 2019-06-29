# app/company_profile.py

# modules
import json # to parse JSON
import csv # to export to CSV
import os # operating system dependent functionality
import datetime

# packages
from dotenv import load_dotenv
import requests
import plotly
import plotly.graph_objs as go

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
    print("Create, modify and track a portfolio of stocks!")
    print("Option 1: Add a ticker to the portfolio")
    print("Option 2: Remove a ticker from the portfolio")
    print("Option 3: View the portfolio")
    print("Option 4: Valuation analysis of your portfolio")
    print("Option 5: Time series analysis of your portfolio")
    print("Option 6: Return to the main screen", "\n")
    portfolio_option = input("Please type a number between 1 and 6: ")  
    while not portfolio_option.isdigit() or int(portfolio_option) > 6 or int(portfolio_option) < 1:
        portfolio_option = input("Incorrect input.  Please type a number between 1 and 6:")
        
    portfolio_option = int(portfolio_option)
    
    test = False 
    if portfolio_option == 1:
        symbol = input("Please enter ticker symbol to add: ")
        request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
        response = requests.get(request_url)
        parsed_response = json.loads(response.text)
        while test == False:
            if len(symbol) > 5:
                symbol = input("Ticker invalid.  Please enter a new ticker: ")
            elif 'Error' in parsed_response.keys():
                symbol = input("Ticker invalid.  Please enter a new ticker: ")
            else:
                investor_portfolio.append(symbol)
                print("\n", "Ticker added to portfolio")
                test = True  

 
    elif portfolio_option == 2:
        while test == False:
            symbol = input("Please enter ticker symbol to delete: ")
            request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
            response = requests.get(request_url)
            parsed_response = json.loads(response.text)
            if len(symbol) > 5:
                symbol = input("Ticker invalid.  Please enter a new ticker: ")
                #request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
                #response = requests.get(request_url)
                #parsed_response = json.loads(response.text) 
            elif 'Error' in parsed_response.keys():
                symbol = input("Ticker invalid.  Please enter a new ticker: ")
                #request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
                #response = requests.get(request_url)
                #parsed_response = json.loads(response.text)
            elif symbol not in investor_portfolio:
                symbol = input("Ticker not in portfolio.  Please enter a new ticker: ")
            else:
                investor_portfolio.remove(symbol)
                print("\n", "Ticker removed from portfolio")  
                test = True
    
    elif portfolio_option == 3:
        print("\n", "Your portfolio contains the following stocks: ", *investor_portfolio)

    elif portfolio_option == 5:
        dates_prices = {}
        if not investor_portfolio:
            print("You do not have a ticker in your portfolio.  Please add a ticker.")
        else:
            for ticker in investor_portfolio: 
                dates_prices[ticker] = {"date":[], "price":[]}
                request_url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?serietype=line"
                response = requests.get(request_url)
                parsed_response = json.loads(response.text)
                dt = parsed_response["historical"]
                for d in dt:
                    dates_prices[ticker]["date"].append(d["date"])
                    dates_prices[ticker]["price"].append(d["close"])
                
                # for line charts code from professor rosetti's "three_charts" exercise was referenced  
                plotly.offline.plot({
                "data": [go.Scatter(x=dates_prices[ticker]["date"], y=dates_prices[ticker]["price"])],
                "layout": go.Layout(title=f"{ticker} Price Chart")
                }, auto_open=True)
                        

                
    
    