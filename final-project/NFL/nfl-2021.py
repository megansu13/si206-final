# Your name: Megan Su
# Your student id: 76790483
# Your email: meganysu@umich.edu
# List who you have worked with on this project: Gunhaar Panjwani and Vasundhara Kulkarni

from bs4 import BeautifulSoup
import http.client
import re
import os
import csv
import unittest
import sqlite3
import json
import requests

# season: take id 
# teams
# IMPORTANT NOTE:

def open_database(db_name):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def get_nfl_data():
    #url = "https://api.sportsdata.io/v3/nfl/scores/json/Standings"
    #headers = {
        #'Ocp-Apim-Subscription-Key': "22dc5861296e4a77857b2909edcd7fa4"
    #}
    #response = requests.get(url, headers=headers)
    #seasons = response.json()

    url2 = f"https://api.sportsdata.io/v3/nfl/scores/json/Standings/2021?"
    headers = {
        'Ocp-Apim-Subscription-Key': "22dc5861296e4a77857b2909edcd7fa4"
    }
    # key=22dc5861296e4a77857b2909edcd7fa4
    response2 = requests.get(url2, headers=headers)
    standings = response2.json()
    standings_dict = {}
    season = 2021
    standings_dict[season] = {}
    #if seasons[season] not in standings_dict:
        #standings_dict[seasons[season]] = {}
        #print('yoohoo')
    for i in range(len(standings)):
        name = standings[i]['Name']
        wins = standings[i]['Wins']
        losses = standings[i]['Losses']
        pointsFor = standings[i]['PointsFor']
        pointsAgainst = standings[i]['PointsAgainst']
        teamID = standings[i]['TeamID']
        if standings[i]['Division'] == "East":
            if "East" not in standings_dict[season]:
                standings_dict[season]["East"] = {}
            standings_dict[season]["East"][name] = {}
            standings_dict[season]["East"][name]["wins"] = wins 
            standings_dict[season]["East"][name]["losses"] = losses 
            standings_dict[season]["East"][name]["for"] = pointsFor
            standings_dict[season]["East"][name]['against'] = pointsAgainst
            standings_dict[season]["East"][name]["id"] = teamID
        elif standings[i]['Division'] == "West":
            if "West" not in standings_dict[season]:
                standings_dict[season]["West"] = {}
            standings_dict[season]["West"][name] = {}
            standings_dict[season]["West"][name]["wins"] = wins 
            standings_dict[season]["West"][name]["losses"] = losses 
            standings_dict[season]["West"][name]["for"] = pointsFor
            standings_dict[season]["West"][name]['against'] = pointsAgainst
            standings_dict[season]["West"][name]["id"] = teamID
        elif standings[i]['Division'] == "North":
            if "North" not in standings_dict[season]:
                standings_dict[season]["North"] = {}
            standings_dict[season]["North"][name] = {}
            standings_dict[season]["North"][name]["wins"] = wins 
            standings_dict[season]["North"][name]["losses"] = losses 
            standings_dict[season]["North"][name]["for"] = pointsFor
            standings_dict[season]["North"][name]['against'] = pointsAgainst
            standings_dict[season]["North"][name]["id"] = teamID
        elif standings[i]['Division'] == "South":
            if "South" not in standings_dict[season]:
                standings_dict[season]["South"] = {}
            standings_dict[season]["South"][name] = {}
            standings_dict[season]["South"][name]["wins"] = wins 
            standings_dict[season]["South"][name]["losses"] = losses 
            standings_dict[season]["South"][name]["for"] = pointsFor
            standings_dict[season]["South"][name]['against'] = pointsAgainst
            standings_dict[season]["South"][name]["id"] = teamID
    #print(seasons[season])
    #print(standings_dict[seasons[season]])
    return standings_dict


def make_nfl_table(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS NFL (id INTEGER PRIMARY KEY, " #had AUTOINCREMENT before
                "season INTEGER, division TEXT, name TEXT, wins INTEGER, losses INTEGER, for INTEGER, against INTEGER)")
    for season in data:  
        for div in data[season]:
            for team in data[season][div]:
                cur.execute("INSERT OR IGNORE INTO NFL (season, division, name, wins, losses, for, against) VALUES (?,?,?,?,?,?,?)",
                            (season, div, team, int(data[season][div][team]["wins"]), int(data[season][div][team]["losses"]), int(data[season][div][team]["for"]), data[season][div][team]["against"],))
    conn.commit()


def main():
    cur, conn = open_database("sports.db")
    data = get_nfl_data()
    make_nfl_table(data, cur, conn)
    
if __name__ == "__main__":
    main()