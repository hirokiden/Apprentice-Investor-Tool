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





###################################### COPY FROM BELOW THIS POINT #####################################################







###################################### Section to input 3 Valid Tickers  ######### 

print("Please enter three valid stock ticker symbols!  As an example, Disney is 'DIS' and AT&T is 'T'. ")
print("The financial data for all three companies will print in three .csv files for your use.")


while True:
    user_input_ticker = input()
    # testuser_input_ticker = input()

    if user_input_ticker.isdigit() == True: # Attributed this line of code concept to prior shopping cart usage 
        # more details located from https://www.tutorialspoint.com/python/string_isdigit.htm, script concept borrowed from website after research
        print("Ticker cannot be a number, please try again")
    elif len(user_input_ticker) > 5:
        print("Ticker cannot exceed 5 characters, please try again")
    else:
        break

while True:
    user_input_ticker2 = input()
    # testuser_input_ticker = input()

    if user_input_ticker2.isdigit() == True: # Attributed this line of code concept to prior shopping cart usage 
        print("Ticker cannot be a number, please try again")
    elif len(user_input_ticker2) > 5:
        print("Ticker cannot exceed 5 characters, please try again")
    else:
        break

while True:
    user_input_ticker3 = input()
    # testuser_input_ticker = input()

    if user_input_ticker3.isdigit() == True: # Attributed this line of code concept to prior shopping cart usage 
        # more details located from https://www.tutorialspoint.com/python/string_isdigit.htm, script concept borrowed from website after research
        print("Ticker cannot be a number, please try again")
    elif len(user_input_ticker3) > 5:
        print("Ticker cannot exceed 5 characters, please try again")
    else:
        break


###################################### Section to store the 3 companies' data from JSON and also assign appropriate variables

batch_financial_statement_request_url = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{user_input_ticker}" #Orig

batch_financial_statement_request_url2 = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{user_input_ticker2}" #2

batch_financial_statement_request_url3 = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{user_input_ticker3}" #3


batch_financial_statement_response = requests.get(batch_financial_statement_request_url) #Orig

batch_financial_statement_response2 = requests.get(batch_financial_statement_request_url2) #2

batch_financial_statement_response3 = requests.get(batch_financial_statement_request_url3) #3



# print(type(response))
# print(response.status_code)
# print(response.text) # This is a string



batch_financial_statement_parsed_response = json.loads(batch_financial_statement_response.text) #this converts string format into dictionary #Orig

batch_financial_statement_parsed_response2 = json.loads(batch_financial_statement_response2.text) #this converts string format into dictionary #1

batch_financial_statement_parsed_response3 = json.loads(batch_financial_statement_response3.text) #this converts string format into dictionary #2

# print(batch_financial_statement_parsed_response["symbol"])
# print(batch_financial_statement_parsed_response2["symbol"])
# print(batch_financial_statement_parsed_response3["symbol"])



###################################### Section to ensure that 3 companies' data are properly connected, if not script will gracefully quit

try: #Orig
    batch_financial_statement_parsed_response["symbol"] 
except:
    print("Invalid ticker(s), please rerun the script and try again")
    exit()

batch_financial_symbols = batch_financial_statement_parsed_response["symbol"] 

batch_financial_list = batch_financial_statement_parsed_response["financials"] 


try: #1
    batch_financial_statement_parsed_response2["symbol"]  
except:
    print("Invalid ticker(s), please rerun the script and try again")
    exit()

batch_financial_symbols2 = batch_financial_statement_parsed_response2["symbol"]

batch_financial_list2 = batch_financial_statement_parsed_response2["financials"]


try: #2
    batch_financial_statement_parsed_response3["symbol"]
except:
    print("Invalid ticker(s), please rerun the script and try again")
    exit()

batch_financial_symbols3 = batch_financial_statement_parsed_response3["symbol"]

batch_financial_list3 = batch_financial_statement_parsed_response3["financials"]

###################################### Section for Testing to ensure all is well

# # print(batch_financial_symbols)
# print(batch_financial_symbols2)
# # print(batch_financial_symbols3)

# # print(batch_financial_list)
# print(batch_financial_list2)
# # print(batch_financial_list3)

# # print(str(batch_financial_symbols).upper())

# ##############################################################################################



# ######################################################### Loop Terminal Printing Testing Area


# # for i in batch_financial_list:
# # #     # print(i["date"], i["Revenue"], i["Revenue Growth"], i["Cost of Revenue"], i["Gross Profit"], 
# # #     # i["R&D Expenses"], i["SG&A Expense"], i["Operating Expenses"] , i["Operating Income"], i["Interest Expense"], i["Earnings before Tax"], 
# # #     # i["Income Tax Expense"], i["Net Income"], i["EPS"], i["EPS Diluted"], i["Dividend per Share"], i["Gross Margin"], i["EBITDA Margin"], i["EBIT Margin"],
# # #     # i["Profit Margin"], i["Free Cash Flow margin"], i["EBITDA"], i[ "EBIT"], i["Consolidated Income"], i["Earnings Before Tax Margin"], i["Net Profit Margin"]
# # #     # )

# #     financial_statement_date = i["date"] #
# #     financial_statement_revenue = i["Revenue"] #
# #     financial_statement_revenue_growth = i["Revenue Growth"] #
# #     financial_statement_cost_revenue = i["Cost of Revenue"] #
# #     financial_statement_gross_profit = i["Gross Profit"] #
# #     financial_statement_rd_exp = i["R&D Expenses"] #
# #     financial_statement_sga_exp = i["SG&A Expense"] #
# #     financial_statement_op_exp = i["Operating Expenses"] #
# #     financial_statement_op_income = i["Operating Income"] # 
# #     financial_statement_int_exp = i["Interest Expense"]
# #     financial_statement_earning_b4_tax = i["Earnings before Tax"]
# #     financial_statement_income_tax_exp = i["Income Tax Expense"]
# #     financial_statement_net_income =  i["Net Income"]
# #     financial_statement_eps = i["EPS"]
# #     financial_statement_eps_diluted = i["EPS Diluted"]
# #     financial_statement_dividend_per_share = i["Dividend per Share"]
# #     financial_statement_gross_margin = i["Gross Margin"]
# #     financial_statement_ebitda_margin = i["EBITDA Margin"]
# #     financial_statement_ebit_margin = i["EBIT Margin"]
# #     financial_statement_profit_margin = i["Profit Margin"]
# #     financial_statement_free_cash_flow_margin = i["Free Cash Flow margin"]
# #     financial_statement_ebidtda = i["EBITDA"]
# #     financial_statement_ebit = i[ "EBIT"]
# #     financial_statement_consolidated_income = i[ "EBIT"]
# #     financial_statement_earnings_b4_tax_margin = i["Earnings Before Tax Margin"]
# #     financial_statement_net_profit_margin = i["Net Profit Margin"]


#     # print(financial_statement_date)
#     # print(financial_statement_revenue)
#     # print(financial_statement_revenue_growth)
#     # print(financial_statement_cost_revenue)
#     # print(financial_statement_gross_profit)
#     # print(financial_statement_rd_exp)
#     # print(financial_statement_sga_exp)
#     # print(financial_statement_op_exp)
#     # print(financial_statement_op_income)
#     # print(financial_statement_int_exp)
#     # print(financial_statement_earning_b4_tax)
#     # print(financial_statement_income_tax_exp)
#     # print(financial_statement_net_income)
#     # print(financial_statement_eps)
#     # print(financial_statement_eps_diluted)
#     # print(financial_statement_dividend_per_share)
#     # print(financial_statement_gross_margin)
#     # print(financial_statement_ebitda_margin)
#     # print( financial_statement_ebit_margin)
#     # print(financial_statement_profit_margin)
#     # print(financial_statement_free_cash_flow_margin)
#     # print(financial_statement_ebidtda)
#     # print(financial_statement_ebit)
#     # print(financial_statement_consolidated_income)
#     # print(financial_statement_earnings_b4_tax_margin)
    # print(financial_statement_net_profit_margin)


##################### Creating .CSV File Paths for the 3 Stock Inputs ##############



# csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "company1financials.csv") # a relative filepath
# # connect script to the .csv file located in the 'data' file
# # prior examples had ".." --> this means go above one directory.  since .py file is in a separate folder 'app', we have to use ".."


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "company1financials.csv") # a relative filepath

csv_file_path2 = os.path.join(os.path.dirname(__file__), "..", "data", "company2financials.csv") # a relative filepath

csv_file_path3 = os.path.join(os.path.dirname(__file__), "..", "data", "company3financials.csv") # a relative filepath

# ##################### Input 1 ####################################################

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    
    csv_headers = ["Ticker", "Date", "Revenue", "Revenue Growth", "Cost of Revenue", "Gross Profit",  "R&D Expenses", "SG&A Expenses",  "Operating Expenses", 
    "Operating Income", "Interest Expense", "Earning before Tax", "Income Tax Expense", "Income Tax Expense",  "Net Income", "EPS", "EPS Diluted",
    "Dividend per Share", "Gross Margin", "EBITDA Margin", "EBIT Margins", "Profit Margin", "Free Cash Flow Margin",  "EBITDA", "EBIT", "Earnings Before Tax Margin",
    "Net Profit Margin"
    ]

    # list out each of the headers via variable
    
    writer = csv.DictWriter(csv_file, fieldnames = csv_headers)
    writer.writeheader() # uses fieldnames set above
   
    for i in batch_financial_list: # This loop will take the 1st ticker and output all the details in the loop
        
        
        financial_statement_date = i["date"] 
        financial_statement_revenue = i["Revenue"] 
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
        "Ticker": str(batch_financial_symbols).upper(), #capitalized the user stock ticker input 1
        "Date":  financial_statement_date, 
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

##################### Input 2 ####################################################

with open(csv_file_path2, "w") as csv_file2: # "w" means "open the file for writing"
    
    csv_headers = ["Ticker", "Date", "Revenue", "Revenue Growth", "Cost of Revenue", "Gross Profit",  "R&D Expenses", "SG&A Expenses",  "Operating Expenses", 
    "Operating Income", "Interest Expense", "Earning before Tax", "Income Tax Expense", "Income Tax Expense",  "Net Income", "EPS", "EPS Diluted",
    "Dividend per Share", "Gross Margin", "EBITDA Margin", "EBIT Margins", "Profit Margin", "Free Cash Flow Margin",  "EBITDA", "EBIT", "Earnings Before Tax Margin",
    "Net Profit Margin"
    ]

    # list out each of the headers via variable
    
    writer = csv.DictWriter(csv_file2, fieldnames = csv_headers)
    writer.writeheader() # uses fieldnames set above
   
    for i in batch_financial_list2: # This loop will take the 2nd ticker and output all the details in the loop
        
        
        financial_statement_date = i["date"] 
        financial_statement_revenue = i["Revenue"] 
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
        "Ticker": str(batch_financial_symbols2).upper(), #capitalized the user stock ticker input 2
        "Date":  financial_statement_date, 
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

##################### Input 3 ####################################################

with open(csv_file_path3, "w") as csv_file3: # "w" means "open the file for writing"
    
    csv_headers = ["Ticker", "Date", "Revenue", "Revenue Growth", "Cost of Revenue", "Gross Profit",  "R&D Expenses", "SG&A Expenses",  "Operating Expenses", 
    "Operating Income", "Interest Expense", "Earning before Tax", "Income Tax Expense", "Income Tax Expense",  "Net Income", "EPS", "EPS Diluted",
    "Dividend per Share", "Gross Margin", "EBITDA Margin", "EBIT Margins", "Profit Margin", "Free Cash Flow Margin",  "EBITDA", "EBIT", "Earnings Before Tax Margin",
    "Net Profit Margin"
    ]

    # list out each of the headers via variable
    
    writer = csv.DictWriter(csv_file3, fieldnames = csv_headers)
    writer.writeheader() # uses fieldnames set above
   
    for i in batch_financial_list3: # This loop will take the 3rd ticker and output all the details in the loop
        
        
        financial_statement_date = i["date"] 
        financial_statement_revenue = i["Revenue"] 
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
        "Ticker": str(batch_financial_symbols3).upper(), #capitalized the user stock ticker input 3
        "Date":  financial_statement_date, 
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
