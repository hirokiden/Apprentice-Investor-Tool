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

# obtain a list of tickers

symbol = input("Please enter ticker symbol, if finished type DONE ")
stop_loop = ["Done","done","DONE"]
investor_data = {}

while symbol not in stop_loop: 
    request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"

    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    test = False

    while test == False:
        if len(symbol) > 5:
            symbol = input("Ticker invalid.  Please enter a new ticker: ")
            request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
            response = requests.get(request_url)
            parsed_response = json.loads(response.text) 
        elif 'Error Message' in parsed_response.keys():
            symbol = input("Ticker invalid.  Please enter a new ticker: ")
            request_url = f"https://financialmodelingprep.com/api/v3/company/profile/{symbol}"
            response = requests.get(request_url)
            parsed_response = json.loads(response.text)
        else: 
            test = True
    
    
    investor_data[symbol] = {"price": [], "beta": [], "vol_avg": [], "mkt_cap": [], "last_div": [], "range": [], "changes": [], "changes_percentage": [], "company_name": [], "exchange": [], "industry": [], "website": [], "description": [], "ceo": [], "sector": [], "image": []}
    
    investor_data[symbol]["price"] = parsed_response["profile"]["price"]
    breakpoint()
    tsd = parsed_response["Time Series (Daily)"]
    dates = list(tsd.keys()) #create a list of all dates
    latest_day = dates[0] #reference the first date which is the most recent
    investor_data[symbol]["last_refreshed"] = parsed_response["Meta Data"]["3. Last Refreshed"]
    investor_data[symbol]["latest_close"] = tsd[latest_day]["4. close"]
    investor_data[symbol]["close_date"] = dates[0]
    
    # find high and low price
    high_prices = []
    low_prices = []

    for date in dates: 
        high_price = tsd[date]["2. high"]
        high_prices.append(float(high_price))
        low_price = tsd[date]["3. low"]
        low_prices.append(float(low_price))

    investor_data[symbol]["recent_high"] = max(high_prices)
    investor_data[symbol]["recent_low"] = min(low_prices)

    if float(investor_data[symbol]["latest_close"]) < float(investor_data[symbol]["recent_low"]) * 1.1:
        investor_data[symbol]["recommendation"] = "BUY"
        investor_data[symbol]["rationale"] = "RECOMMENDATION REASON: PRICE 110 PERCENT OF THE LOW OR LESS"
    if float(investor_data[symbol]["latest_close"]) > float(investor_data[symbol]["recent_high"]) * 1.1:
        investor_data[symbol]["recommendation"] = "SELL"
        investor_data[symbol]["rationale"] = "RECOMMENDATION REASON: PRICE GREATER THAN 110 PERCENT OF HIGH"
    else:
        investor_data[symbol]["recommendation"] = "HOLD"
        investor_data[symbol]["rationale"] = "STOCK DOES NOT APPEAR TO BE AT DISCOUNT OR OVERPRICED"

    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", symbol + ".csv")

    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
    with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers, lineterminator='\r')
        writer.writeheader() # uses fieldnames set above
        for date in dates:
            prices = {}
            daily_prices = tsd[date]
            writer.writerow({
                "timestamp": date, 
                "open": to_usd(float(daily_prices["1. open"])),
                "high": to_usd(float(daily_prices["2. high"])),
                "low": to_usd(float(daily_prices["3. low"])),
                "close": to_usd(float(daily_prices["4. close"])),
                "volume": daily_prices["5. volume"]
            })
    symbol = input("Please enter another ticker or type 'DONE': ")

symbol_keys = list(investor_data.keys())

now = datetime.datetime.now()
dt_string = now.strftime("%m/%d/%Y %I:%M:%S %p")

print("\n")
print("-------------------------")
print("REQUEST AT:", dt_string)
print("-------------------------")


for key in symbol_keys:

    print("\n")
    print("-------------------------")
    print(f"Stock Ticker: {key}")
    print("-------------------------")
    print("LATEST DAY: ", investor_data[key]["last_refreshed"])
    print("LATEST CLOSE: ", to_usd(float(investor_data[key]["latest_close"])))
    print("RECENT HIGH: ", to_usd(float(investor_data[key]["recent_high"])))
    print("RECENT LOW: ", to_usd(float(investor_data[key]["recent_low"])))
    print("-------------------------")
    print("RECOMMENDATION: ", investor_data[key]["recommendation"])
    print("RATIONALE: ", investor_data[key]["rationale"])
 

    print("-------------------------")
    #print(f"DATA WRITTEN TO 'PRICES.CSV': {csv_file_path}...")
    print("-------------------------")


print("\n")