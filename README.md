# Apprentice-Investor-Tool

# Overview

The goal of the ‘Apprentice Investor Tool’ is to provide a user an interactive tool that can provide immediate, uncluttered and relevant business and economic information/data.  Data includes company valuations, financial statements, key metrics, company financial data via .csv files for research purposes, stock prices and associated charting, performance of major indexes, most active stocks, the top gainers and losers, sector performances, foreign exchange rates, cryptocurrency performance and list of calendar year holidays.  SendGrid email functionality is also included to email the user with a list of stocks in the portfolio and current prices.

# Create a new environment

conda create -n appinv-env python=3.7 # (first time only)
conda activate appinv-env

# From within the virtual environment install the following packages

pip install requests
pip install plotly
pip install requirements.txt
pip install sendgrid==6.0.5
pip install dotenv

# Initial Setup

Use Github.com to  fork the existing tool located at https://github.com/hirokiden/Apprentice-Investor-Tool).  

Once your repository is created you should be able to view it at the following path (assuming the name "Apprentice-Tool" was used):
https://github.com/YOUR_USERNAME/apprentice-tool. 

Make sure that your copied repository includes a .gitignore file that excludes your personal .env file with sensitive credentials. 

After creating the repo use Github Desktop or the command line to clone it to your computer.  Make sure to save the file in a familiar location.

Use the command line to navigate to the location of the program (the python program should be located in a folder titled "app").

Instructions to sign up for SendGrid account:

"First, sign up for a free account, then click the link in a confirmation email to verify your account. Then create an API Key with "full access" permissions.

To setup the usage examples below, store the API Key value in an environment variable called SENDGRID_API_KEY. Also set an environment variable called MY_EMAIL_ADDRESS to be the email address you just associated with your SendGrid account (e.g. "abc123@gmail.com")."

Sourced from Professor Mike Rosetti (NYU Stern Professor): https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/sendgrid.md

Create a .env file and copy and paste your credentials (example below)
SENDGRID_API_KEY = "xxxxxxxexamplexxxxxxx"
MY_EMAIL_ADDRESS = "example1@stern.nyu.edu"
TO_EMAIL_ADDRESS = "example2@stern.nyu.edu"
SENDGRID_TEMPLATE_ID = "123example"


Once logged onto SendGrid, the below code can be used to setup the custom template:

<img src="https://i.ibb.co/svxhJST/MDM.png">

<h3>Please see below your current portfolio with APPRENTICE INVESTOR:</h3>

<p>Date: {{timestamp}}</p>

<ul>
{{#each products}}
	<li>Company: {{this.name}}</li>
	<li>Price: {{this.price}}</li>
	<br>
{{/each}}
</ul>

Once complete, you should be able to send custom emails.

# Run the program from the command line

python app/apprentice.py

# Successful Run

If the program runs successfully, you should be provided the following options:

Option 1: Add a ticker to the portfolio
Option 2: Remove a ticker from the portfolio
Option 3: View the portfolio
Option 4: Company Profile of your portfolio
Option 5: Time series analysis of your portfolio
Option 6: Current Market Information
Option 7: Send yourself an email with your stocks and current prices
Option 8: List of available market data functions

"Option 1" must be selected first before selecting Options 2 - 5, as the portfolio must be created before any other portfolio specific action can be taken.

"Option 8" will provide an additional list of options to view market information.  A portfolio does not need to exist for these options to be run.

# Versioning 

See different versions at this repository:

https://github.com/hirokiden/Apprentice-Investor-Tool/commits/master

# Authors

Hiroki Den
Rob Sansone

# License

This project was licensed under an MIT license

# Acknowledgements

Financial Data was sourced from financialmodelingprep.com

Professor Mike Rosetti's NYU Stern material was referenced frequently, located here:
https://github.com/prof-rossetti/nyu-info-2335-201905


