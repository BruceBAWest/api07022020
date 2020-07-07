#!/usr/bin/eng python3
import requests
import sys
import json
import webbrowser 

# add date for game a nsend request
nhl = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

if nhl.status_code == 200:
    game = nhl.json()
else:
    print(f'Invlaid Request - response code {nhl.status_code}')
    sys.exit("Unable to process response") # only ditch if the response is not a 200 code

# input nhl team's 3-letter abbreviation
abrv = input("NHL Team Abreviation: ")

# match input nhl 3-letter abbreviation
for team in game['teams']:
    if abrv == team['abbreviation']:
        print("you have a match")
        webbrowser.open(team['officialSiteUrl'])


