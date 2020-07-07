#!/usr/bin/env python3

"""
author: brucebawest
nhl api with pandas
"""

import requests
import pandas as pd
from pandas.io.json import json_normalize

ADDRESS = "https://statsapi.web.nhl.com/api/v1/teams"

def main():

    ########### Test for accessing data  ##########
    response = requests.get(ADDRESS)
    responseData = response.json()

    for data in responseData["teams"]:
        print(data["id"], end = " : ")
        print(data["name"], end = " : ")
        print(data["link"], end = " : ")
        print(data["venue"]["name"])


    ########### Use Pandas to process the data ###########
    # Take the JSON data
    dataPandas = pd.read_json(ADDRESS)
    
    # Normalize the JSON
    normalizedDataPandas= json_normalize(dataPandas["teams"])
    
    # Test for sorting data
    test =  normalizedDataPandas.sort_values(by = ['firstYearOfPlay'])
   
    # Sort by 'FirstYearOfPlay' and display "name" and "firstYearOfPlay"
    print(normalizedDataPandas.sort_values(by = ['firstYearOfPlay']).iloc[:51,[normalizedDataPandas.columns.get_loc("name"), normalizedDataPandas.columns.get_loc("firstYearOfPlay")]])
main()
