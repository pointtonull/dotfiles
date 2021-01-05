#!/usr/bin/python3

import csv

import requests

URL = "https://projects.fivethirtyeight.com/soccer-api/international/2018/wc_matches.csv"

response = requests.get(URL)
reader = csv.DictReader(response.text.splitlines())

for match in reader:
    if not match["score1"]:
        print("    {team1: >20} {proj_score1:4} - {proj_score2:4} {team2: <20}".format(
            **match))
    else:
        print("{team1: >20} ({proj_score1:4}) {score1} - {score2} ({proj_score2:4}) {team2: <20}".format(
            **match))

