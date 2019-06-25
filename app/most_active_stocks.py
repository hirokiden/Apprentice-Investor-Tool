# python most_active_stocks.py


#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

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
# print(get_jsonparsed_data(url))


most_active_parser_response = get_jsonparsed_data(url)


# print(most_active_parser_response)

# print(most_active_parser_response)

for i in most_active_parser_response["mostActiveStock"]:
    print(i["mostActiveStock"]["ticker"])

# for i in stock_sectors_parsed_response["sectorPerformance"]:
#     print(i["sector"], i["changesPercentage"])