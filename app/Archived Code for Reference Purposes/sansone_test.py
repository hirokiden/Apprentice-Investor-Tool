#  python market_comp_csv_printer.py

import os
import requests
import json # need this to import json string into dictionary
from datetime import datetime # taken from stackoverflow
import csv # so you can write date to .csv

def usd_format(my_price):
    return "${0:,.2f}".format(my_price) # This UDF will change numerical denomination to currency and cents (2 digits) format when passed through


investor_portfolio = ["MS", "MSFT"]

for ticker in investor_portfolio:
    fs_request_url = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{ticker}"
    fs_response = requests.get(fs_request_url)
    parsed_response = json.loads(fs_response.text)
    fs = parsed_response["financials"]

    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", ticker + ".csv") # a relative filepath

    with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    
        csv_headers = ["Ticker", "Date", "Revenue", "Revenue Growth", "Cost of Revenue", "Gross Profit",  "R&D Expenses", "SG&A Expenses",  "Operating Expenses", 
        "Operating Income", "Interest Expense", "Earning before Tax", "Income Tax Expense", "Income Tax Expense",  "Net Income", "EPS", "EPS Diluted",
        "Dividend per Share", "Gross Margin", "EBITDA Margin", "EBIT Margins", "Profit Margin", "Free Cash Flow Margin",  "EBITDA", "EBIT", "Earnings Before Tax Margin",
        "Net Profit Margin"
        ]

    
        writer = csv.DictWriter(csv_file, fieldnames = csv_headers, lineterminator = '\r')
        writer.writeheader() # uses fieldnames set above
   
        for i in fs: # This loop will take the 1st ticker and output all the details in the loop


            writer.writerow({
            "Ticker": ticker.upper(), #capitalized the user stock ticker input 1
            "Date":  i["date"] , 
            "Revenue": i["Revenue"] , 
            "Revenue Growth": i["Revenue Growth"], 
            "Cost of Revenue":  i["Cost of Revenue"], 
            "Gross Profit": i["Gross Profit"], 
            "R&D Expenses": i["R&D Expenses"], 
            "SG&A Expenses": i["SG&A Expense"], 
            "Operating Expenses": i["Operating Expenses"] , 
            "Operating Income": i["Operating Income"], 
            "Interest Expense": i["Interest Expense"], 
            "Earning before Tax": i["Earnings before Tax"], 
            "Income Tax Expense": i["Income Tax Expense"], 
            "Net Income": i["Net Income"], 
            "EPS": i["EPS"], 
            "EPS Diluted": i["EPS Diluted"], 
            "Dividend per Share": i["Dividend per Share"], 
            "Gross Margin": i["Gross Margin"], 
            "EBITDA Margin": i["EBITDA Margin"], 
            "EBIT Margins":  i["EBIT Margin"], 
            "Profit Margin": i["Profit Margin"], 
            "Free Cash Flow Margin": i["Free Cash Flow margin"], 
            "EBITDA": i["EBITDA"], 
            "EBIT": i["EBIT"], 
            "Earnings Before Tax Margin": i["Earnings Before Tax Margin"], 
            "Net Profit Margin": i["Net Profit Margin"],
        
            
            })

