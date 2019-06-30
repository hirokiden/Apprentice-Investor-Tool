# Apprentice-Investor-Tool

# Overview

The goal of the ‘Apprentice Investor Tool’ is to provide a user an interactive tool that can provide immediate, uncluttered and relevant business and economic information/data.  Data include company valuations, financial statements, key metrics, outputting company data via .csv files for research purposes, stock prices and associated charting, performance of major indexes, most active stocks, the top gainers and losers, sector performances, foreign exchange rates, cryptocurrency performance and list of calendar year holidays.  

# Initial Setup

Use Github.com to  fork the existing tool located at https://github.com/hirokiden/Apprentice-Investor-Tool).  

Once your repository is created you should be able to view it at the following path (assuming the name "Apprentice-Tool" was used):
https://github.com/YOUR_USERNAME/apprentice-tool. 

After creating the repo use Github Desktop or the command line to clone it to your computer.  Make sure to save the file in a familiar location.

Use the command line to navigate to the location of the program.

# Create a new environment

conda create -n appinv-env python=3.7 # (first time only)
conda activate appinv-env

# From within the virtual environment install the following packages

pip install requests
pip install plotly

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

"Option 1" must be selected first before selecting Options 2 - 5, as the portfolio must be created before any other portfolio specific action can be taken.

"Option 6" will provide an additional list of options to view market information.  A portfolio does not need to exist for these options to be run.

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
Professor Rosetti's NYU Stern material was referenced frequently
