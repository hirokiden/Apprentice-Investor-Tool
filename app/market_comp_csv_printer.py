#  python market_comp_csv_printer.py



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

print("Please enter a valid stock ticker symbol!  As an example, Disney is 'DIS' and AT&T is 'T'. ")


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

################################################################################################################################################

list_of_financial_statement_dates = list(batch_financial_list) # convert the dates dictionary keys into list format

# print(list_of_financial_statement_dates)

# print( list_of_financial_statement_dates[:500] )

################################################################################################################################################

# print(batch_financial_list)


for i in batch_financial_list:
#     # print(i["date"], i["Revenue"], i["Revenue Growth"], i["Cost of Revenue"], i["Gross Profit"], 
#     # i["R&D Expenses"], i["SG&A Expense"], i["Operating Expenses"] , i["Operating Income"], i["Interest Expense"], i["Earnings before Tax"], 
#     # i["Income Tax Expense"], i["Net Income"], i["EPS"], i["EPS Diluted"], i["Dividend per Share"], i["Gross Margin"], i["EBITDA Margin"], i["EBIT Margin"],
#     # i["Profit Margin"], i["Free Cash Flow margin"], i["EBITDA"], i[ "EBIT"], i["Consolidated Income"], i["Earnings Before Tax Margin"], i["Net Profit Margin"]
#     # )

    financial_statement_date = i["date"] #
    financial_statement_revenue = i["Revenue"] #
    financial_statement_revenue_growth = i["Revenue Growth"] #
    financial_statement_cost_revenue = i["Cost of Revenue"] #
    financial_statement_gross_profit = i["Gross Profit"] #
    financial_statement_rd_exp = i["R&D Expenses"] #
    financial_statement_sga_exp = i["SG&A Expense"] #
    financial_statement_op_exp = i["Operating Expenses"] #
    financial_statement_op_income = i["Operating Income"] # 
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


    # print(financial_statement_date)
    # print(financial_statement_revenue)
    # print(financial_statement_revenue_growth)
    # print(financial_statement_cost_revenue)
    # print(financial_statement_gross_profit)
    # print(financial_statement_rd_exp)
    # print(financial_statement_sga_exp)
    # print(financial_statement_op_exp)
    # print(financial_statement_op_income)
    # print(financial_statement_int_exp)
    # print(financial_statement_earning_b4_tax)
    # print(financial_statement_income_tax_exp)
    # print(financial_statement_net_income)
    # print(financial_statement_eps)
    # print(financial_statement_eps_diluted)
    # print(financial_statement_dividend_per_share)
    # print(financial_statement_gross_margin)
    # print(financial_statement_ebitda_margin)
    # print( financial_statement_ebit_margin)
    # print(financial_statement_profit_margin)
    # print(financial_statement_free_cash_flow_margin)
    # print(financial_statement_ebidtda)
    # print(financial_statement_ebit)
    # print(financial_statement_consolidated_income)
    # print(financial_statement_earnings_b4_tax_margin)
    # print(financial_statement_net_profit_margin)


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "company1financials.csv") # a relative filepath
# connect script to the .csv file located in the 'data' file
# prior examples had ".." --> this means go above one directory.  since .py file is in a separate folder 'app', we have to use ".."



with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    
    csv_headers = ["date", "Revenue", "Revenue Growth", "Cost of Revenue", "Gross Profit",  "R&D Expenses", "SG&A Expenses",  "Operating Expenses", 
    "Operating Income", "Interest Expense", "Earning before Tax", "Income Tax Expense", "Income Tax Expense",  "Net Income", "EPS", "EPS Diluted",
    "Dividend per Share", "Gross Margin", "EBITDA Margin", "EBIT Margins", "Profit Margin", "Free Cash Flow Margin",  "EBITDA", "EBIT", "Earnings Before Tax Margin",
    "Net Profit Margin"
    ]

    # list out each of the headers via variable
    
    writer = csv.DictWriter(csv_file, fieldnames = csv_headers)
    writer.writeheader() # uses fieldnames set above
   
    for i in batch_financial_list: # set a loop up for the dictionary, for each date, write out the headers above for each row, repeat until end of page
        

        writer.writerow({
        "date":  financial_statement_date, 
        "Revenue": financial_statement_revenue, 
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




    # financial_statement_revenue_growth = i["Revenue Growth"] #
    # financial_statement_cost_revenue = i["Cost of Revenue"] #
    # financial_statement_gross_profit = i["Gross Profit"] #
    # financial_statement_rd_exp = i["R&D Expenses"] #
    # financial_statement_sga_exp = i["SG&A Expense"] #
    # financial_statement_op_exp = i["Operating Expenses"] #
    # financial_statement_op_income = i["Operating Income"] # 
    # financial_statement_int_exp = i["Interest Expense"]
    # financial_statement_earning_b4_tax = i["Earnings before Tax"]
    # financial_statement_income_tax_exp = i["Income Tax Expense"]
    # financial_statement_net_income =  i["Net Income"]
    # financial_statement_eps = i["EPS"]
    # financial_statement_eps_diluted = i["EPS Diluted"]
    # financial_statement_dividend_per_share = i["Dividend per Share"]
    # financial_statement_gross_margin = i["Gross Margin"]
    # financial_statement_ebitda_margin = i["EBITDA Margin"]
    # financial_statement_ebit_margin = i["EBIT Margin"]
    # financial_statement_profit_margin = i["Profit Margin"]
    # financial_statement_free_cash_flow_margin = i["Free Cash Flow margin"]
    # financial_statement_ebidtda = i["EBITDA"]
    # financial_statement_ebit = i[ "EBIT"]
    # financial_statement_consolidated_income = i[ "EBIT"]
    # financial_statement_earnings_b4_tax_margin = i["Earnings Before Tax Margin"]
    # financial_statement_net_profit_margin = i["Net Profit Margin"]

# with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    
#     csv_headers = ["TimeStamp", "Open", "High", "Low", "Close", "Volume"] # list out each of the headers via variable
#     writer = csv.DictWriter(csv_file, fieldnames = csv_headers)
#     writer.writeheader() # uses fieldnames set above
   
#     for date in dates_list: # set a loop up for the dates_list, for each date, write out the headers above for each row, repeat until end of page
#         daily_performance = parsed_response["Time Series (Daily)"][date]

#         writer.writerow({
#         "TimeStamp": date, 
#         "Open": daily_performance["1. open"], 
#         "High": daily_performance["2. high"], 
#         "Low": daily_performance["3. low"], 
#         "Close": daily_performance["4. close"], 
#         "Volume": daily_performance["5. volume"] 
        
#         })
