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
    print("Option 4: Company Profile of your portfolio")
    print("Option 5: Time series analysis of your portfolio")
    print("Option 6: Current Market Information", "\n")
    portfolio_option = input("Please type a number between 1 and 6: ")  
    while not portfolio_option.isdigit() or int(portfolio_option) > 6 or int(portfolio_option) < 1:
        portfolio_option = input("Incorrect input.  Please type a number between 1 and 6:")
        
    portfolio_option = int(portfolio_option)
    
    test = False 
    if portfolio_option == 1:
        symbol = input("Please enter ticker symbol to add: ")
        while test == False:
            request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
            response = requests.get(request_url)
            parsed_response = json.loads(response.text)
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
            elif 'Error' in parsed_response.keys():
                symbol = input("Ticker invalid.  Please enter a new ticker: ")
            elif symbol not in investor_portfolio:
                symbol = input("Ticker not in portfolio.  Please enter a new ticker: ")
            else:
                investor_portfolio.remove(symbol)
                print("\n", "Ticker removed from portfolio")  
                test = True

    elif portfolio_option == 3:
        print("\n", "Your portfolio contains the following stocks: ", *investor_portfolio)
   
    elif portfolio_option == 4:
        if not investor_portfolio:
            print("You do not have a ticker in your portfolio.  Please add a ticker.")
        else:
            for ticker in investor_portfolio:
                request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{ticker}"
                response = requests.get(request_url)
                parsed_response = json.loads(response.text)
                cp = parsed_response["profile"]
                print("\n")
                print(cp["companyName"], "Company Profile")
                print("\n")
                print("Beta: ", cp["beta"])
                print("Average Volume: ", cp["volAvg"])
                print("Market Cap: ", cp["mktCap"])
                print("Last Dividend: ", cp["lastDiv"])
                print("Change: ", cp["changes"])
                print("Change Percentage: ", cp["changesPercentage"])
                print("Exchange: ", cp["exchange"])
                print("Industry: ", cp["industry"])
                print("Website: ", cp["website"])
                print("Desciption: ", cp["description"])
                print("CEO: ", cp["ceo"])
                print("Sector: ", cp["sector"])
                print("Image: ", cp["image"])
    
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
    
    elif portfolio_option == 6:
        print("\n")
        print("Choose one of the following options: ")
        print("Option 1: Market Open Close")
        print("Option 2: Daily Stock Sectors")
        print("Option 3: Index List")
        print("Option 4: Most Active Stocks")
        print("Option 5: Biggest Gainer Stocks")
        print("Option 6: Biggest Losers Stocks")
        print("Option 7: Forex Current Rates")    
        print("Option 8: Crypto Currencies")
        print("Option 9: Crytpo Ticker")
        print("\n")        
            
        market_option = input("Please type a number between 1 and 9: ")  
        while not market_option.isdigit() or int(market_option) > 9 or int(market_option) < 1:
            market_option = input("Incorrect input.  Please type a number between 1 and 9:")
            
        market_option = int(market_option)
         
        if market_option == 1:

            market_open_close_request_url = f"https://financialmodelingprep.com/api/v3/is-the-market-open"

            market_open_close_response = requests.get(market_open_close_request_url)

            market_open_close_parsed_response = json.loads(market_open_close_response.text) #this converts string format into dictionary

            if market_open_close_parsed_response["isTheStockMarketOpen"] == "True":
                open_or_not = "Open"
            else:
                open_or_not = "Closed" 

            this_calendar_year = market_open_close_parsed_response["stockMarketHolidays"][0]

            print("The", market_open_close_parsed_response["stockExchangeName"], "opens at", market_open_close_parsed_response["stockMarketHours"]["openingHour"], "and closes at", market_open_close_parsed_response["stockMarketHours"]["closingHour"], "on weekdays.")
            print("\n")
            print("The Stock Market is currently", open_or_not,".")
            print("Note that these are the upcoming holidays for the current Calendar Year:", this_calendar_year["year"])

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

        if market_option == 2:

            stock_sectors_request_url = f"https://financialmodelingprep.com/api/v3/stock/sectors-performance"
            stock_sectors_response = requests.get(stock_sectors_request_url)
            stock_sectors_parsed_response = json.loads(stock_sectors_response.text) #this converts string format into dictionary

            print("The following list contains a comprehensive daily snapshot of industrial sectors' performance:")

            for i in stock_sectors_parsed_response["sectorPerformance"]:

                daily_sector_name = i["sector"]
                daily_sector_pct_change = i["changesPercentage"]

                print("\n")
                print("Sector Name:", daily_sector_name)
                print("Change in %:", daily_sector_pct_change)
                print(i["sector"], i["changesPercentage"])
        
        if market_option == 3:

            index_list_request_url = f"https://financialmodelingprep.com/api/v3/majors-indexes"
            index_list_response = requests.get(index_list_request_url)
            index_list_parsed_response = json.loads(index_list_response.text) #this converts string format into dictionary

            for i in index_list_parsed_response["majorIndexesList"]:
                print("\n")
                ticker = i["ticker"]
                index_name = i["indexName"]
                price = i["price"]
                changes = i["changes"]
                
                print(ticker)
                print (index_name)
                print("Index Price: $", price)
                print("Index Change: $", changes)


