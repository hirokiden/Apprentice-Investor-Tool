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

        if market_option == 4:
            now = datetime.datetime.now()
            date_time = now.strftime("%m/%d/%Y %I:%M:%S %p")
            try:
                from urllib.request import urlopen
            except ImportError:
                from urllib2 import urlopen

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
            most_active_parser_response = get_jsonparsed_data(url)

            print("You are pulling this information at:", date_time)
            print("The Most Active Stocks Traded Are:")

            for k in most_active_parser_response.keys():
                ticker = most_active_parser_response[k]
                mas_ticker = ticker["Ticker"]
                mas_price = ticker["Price"]
                mas_change = ticker["Changes"]
                mas_change_pct = ticker["ChangesPerc"]
                mas_comp_name = ticker["companyName"]

                print("\n")
                print("Stock Ticker:", mas_ticker)
                print("Company Name:", mas_comp_name)
                print("Current Price:", to_usd(float(mas_price) ) )
                print("Price Change:", to_usd(float(mas_change) ) )
                print("Price Change %:", mas_change_pct)
    
        if market_option == 5:

            most_gainer_request_url = f"https://financialmodelingprep.com/api/v3/stock/gainers"

            most_gainer_response = requests.get(most_gainer_request_url)

            most_gainer_parsed_response = json.loads(most_gainer_response.text) #this converts string format into dictionary

            for i in most_gainer_parsed_response["mostGainerStock"]:
    
                mgs_ticker = i["ticker"]
                mgs_price = i["price"]
                mgs_changes = i["changes"]
                mgs_change_pct = i["changesPercentage"]
                mgs_company_name = i["companyName"]

                print("\n")
                print("Stock Ticker:", mgs_ticker)
                print("Company Name:", mgs_company_name)
                print("Current Price:", to_usd(float(mgs_price)))
                print("Price Change:", to_usd(float(mgs_changes)))
                print("Price Change %:", mgs_change_pct)
            
        if market_option == 6:
            most_loser_request_url = f"https://financialmodelingprep.com/api/v3/stock/losers"

            most_loser_response = requests.get(most_loser_request_url)

            most_loser_parsed_response = json.loads(most_loser_response.text) #this converts string format into dictionary

            for i in most_loser_parsed_response["mostLoserStock"]:
                mls_ticker = i["ticker"]
                mls_price = i["price"]
                mls_changes = i["changes"]
                mls_change_pct = i["changesPercentage"]
                mls_companyname = i["companyName"]

                print("\n")
                print("Stock Ticker:", mls_ticker)
                print("Company Name:", mls_companyname)
                print("Current Price:", float(mls_price))
                print("Price Change:", float(mls_changes))
                print("Price Change %:", mls_change_pct)

        if market_option == 7:
            forex_request_url = f"https://financialmodelingprep.com/api/v3/forex"

            forex_response = requests.get(forex_request_url)

            forex_parsed_response = json.loads(forex_response.text) #this converts string format into dictionary

            print("The following list contains a comprehensive daily snapshot of major currencies' Forex:")

            for i in forex_parsed_response["forexList"]:

                forex_ticker = i["ticker"]
                forex_bid = i["bid"]
                forex_ask = i["ask"]
                forex_open = i["open"]
                forex_low = i["low"]
                forex_high = i["high"]
                forex_changes = i["changes"]
                forex_date = i["date"]


                print("\n")
                print("Forex Tickers:", forex_ticker)
                print("Forex Bid:", forex_bid)
                print("Forex Ask:", forex_ask)
                print("Forex Open:", forex_open)
                print("Forex Low:", forex_low)
                print("Forex High", forex_high)
                print("Forex Change:", forex_changes)
                print("Forex Date:", forex_date)

        if market_option == 8:

            crypto_list_request_url = f"https://financialmodelingprep.com/api/v3/cryptocurrencies"

            crypto_list_response = requests.get(crypto_list_request_url)

            crypto_list_parsed_response = json.loads(crypto_list_response.text) #this converts string format into dictionary

            print("The following list contains a comprehensive daily snapshot of major cryptocurrecies' performance:")

            for i in crypto_list_parsed_response["cryptocurrenciesList"]:
                print(i["ticker"], i["name"], i["price"], i["changes"], i["marketCapitalization"])


        if market_option == 9:

            ticker_loop = 0
            while ticker_loop == 0:
                bitcoin_ticker = input("Please enter your desired crypto ticker: ")

                bitcoin_ticker_lower= bitcoin_ticker.lower()

                crypto_list_request_url = f"https://financialmodelingprep.com/api/v3/cryptocurrency/{bitcoin_ticker_lower}"

                crypto_list_parsed_response = requests.get(crypto_list_request_url)
                crypto_list_parsed_response = json.loads(crypto_list_parsed_response.text) #this converts string format into dictionary
                
                try: 
                    crypto_list_parsed_response["ticker"]
                    ticker_loop = 1
                except:
                    print("Crypto ticker invalid.  Please enter another Crypto ticker: ")
                    

            selected_crypo_ticker = crypto_list_parsed_response["ticker"]
            selected_crypo_name = crypto_list_parsed_response[ "name"]
            selected_crypo_price = crypto_list_parsed_response[ "price"]
            selected_crypo_change = crypto_list_parsed_response[ "changes"]
            selected_crypo_market_cap = crypto_list_parsed_response[ "marketCapitalization"]

            print("\n")
            print("Cryptocurrency Ticker:", selected_crypo_ticker)
            print("Cryptocurrency Name:", selected_crypo_name)
            print("Current Price: $", float(selected_crypo_price) ) 
            print("Price Change:", to_usd( float(selected_crypo_change) ) )
            print("Market Capitalization:", to_usd( float(selected_crypo_market_cap) ) )

