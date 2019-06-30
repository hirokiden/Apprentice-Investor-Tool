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

            financial_statement_revenue_growth = i["Revenue Growth"] 
            financial_statement_cost_revenue = i["Cost of Revenue"] 
            financial_statement_gross_profit = i["Gross Profit"] 
            financial_statement_rd_exp = i["R&D Expenses"] 
            financial_statement_sga_exp = i["SG&A Expense"] 
            financial_statement_op_exp = i["Operating Expenses"] 
            financial_statement_op_income = i["Operating Income"] 
            financial_statement_int_exp = i["Interest Expense"]
            financial_statement_earning_b4_tax = i["Earnings before Tax"]
            financial_statement_income_tax_exp = i["Income Tax Expense"]
            financial_statement_net_income =  i["Net Income"]
            financial_statement_eps = i["EPS"]
            financial_statement_eps_diluted = i["EPS Diluted"]
            financial_statement_dividend_per_share = i["Dividend per Share"]
            financial_statement_gross_margin = i["Gross Margin"]
            financial_statement_ebitda_margin = i["EBITDA Margin"]
            financial_statement_ebit_margin = i["EBIT Margin"]
            financial_statement_profit_margin = i["Profit Margin"]
            financial_statement_free_cash_flow_margin = i["Free Cash Flow margin"]
            financial_statement_ebidtda = i["EBITDA"]
            financial_statement_ebit = i[ "EBIT"]
            financial_statement_consolidated_income = i[ "EBIT"]
            financial_statement_earnings_b4_tax_margin = i["Earnings Before Tax Margin"]
            financial_statement_net_profit_margin = i["Net Profit Margin"]


            writer.writerow({
            "Ticker": ticker.upper(), #capitalized the user stock ticker input 1
            "Date":  i["date"] , 
            "Revenue": i["Revenue"] , 
            "Revenue Growth": financial_statement_revenue_growth, 
            "Cost of Revenue":  financial_statement_cost_revenue, 
            "Gross Profit": financial_statement_gross_profit, 
            "R&D Expenses": financial_statement_rd_exp, 
            "SG&A Expenses": financial_statement_sga_exp, 
            "Operating Expenses": financial_statement_op_exp, 
            "Operating Income": financial_statement_op_income, 
            "Interest Expense": financial_statement_int_exp, 
            "Earning before Tax": financial_statement_earning_b4_tax, 
            "Income Tax Expense": financial_statement_income_tax_exp, 
            "Net Income": financial_statement_net_income, 
            "EPS": financial_statement_eps, 
            "EPS Diluted": financial_statement_eps_diluted, 
            "Dividend per Share": financial_statement_dividend_per_share, 
            "Gross Margin": financial_statement_gross_margin, 
            "EBITDA Margin": financial_statement_ebitda_margin, 
            "EBIT Margins":  financial_statement_ebit_margin, 
            "Profit Margin": financial_statement_profit_margin, 
            "Free Cash Flow Margin": financial_statement_free_cash_flow_margin, 
            "EBITDA": financial_statement_ebidtda, 
            "EBIT": financial_statement_ebit, 
            "Earnings Before Tax Margin": financial_statement_earnings_b4_tax_margin, 
            "Net Profit Margin": financial_statement_net_profit_margin,
        
            
            })

