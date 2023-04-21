# Your name: Vasundhara Kulkarni
# Your student id: 01211840
# Your email: kulkvasu@umich.edu
# List who you have worked with on this project: Gunhaar Panjwani and Megan Su

from bs4 import BeautifulSoup
import http.client
import re
import os
import csv
import unittest
import sqlite3
import json
import requests

# For Basketball Sports KEY: 78776eefec674c20ea9530f0e4d0b9cd
# IMPORTANT NOTE:

def open_database(db_name):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def get_basketball_data():
    url = "https://v1.basketball.api-sports.io/leagues?name=NBA"
    headers = {
        'x-rapidapi-host': "v1.basketball.api-sports.io",
        'x-rapidapi-key': "78776eefec674c20ea9530f0e4d0b9cd"
    }
    idList = {1, 3}
    standings_dict = {}
    for id in idList:
        idUrl = f"https://v1.basketball.api-sports.io/standings?league={id}&season=2019-2020"
        idResponse = requests.get(idUrl, headers=headers)
        idStandings = idResponse.json()
        idLeagueName = idStandings["response"][0][0]['stage']
        standings_dict[idLeagueName] = {}
        for i in range(len(idStandings["response"][0])):
            position = idStandings['response'][0][i]['position']
            teamName = idStandings['response'][0][i]['team']['name']
            forPoints = idStandings['response'][0][i]['points']['for']
            against = idStandings['response'][0][i]['points']['against']
            leagueID = idStandings['response'][0][i]['league']['id']
            if idStandings['response'][0][i]['group']['name'] == "Regular Season":
                if "Regular Season" not in standings_dict[idLeagueName]:
                    standings_dict[idLeagueName]["Regular Season"] = {}
                
                standings_dict[idLeagueName]["Regular Season"][teamName] = {}
                standings_dict[idLeagueName]["Regular Season"][teamName]["position"] = position 
                standings_dict[idLeagueName]["Regular Season"][teamName]["for"] = forPoints
                standings_dict[idLeagueName]["Regular Season"][teamName]['id'] = leagueID
                standings_dict[idLeagueName]["Regular Season"][teamName]["against"] = against
    return standings_dict

def make_basketball_table(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Basketball (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "conference TEXT, teamName TEXT, name TEXT, forPoints INTEGER, againstPoints INTEGER, position INTEGER)")
    for conf in data:
        for group in data[conf]:
            for team in data[conf][group]:
                cur.execute("INSERT OR IGNORE INTO Basketball (conference, teamName, name, forPoints, againstPoints, position) VALUES (?,?,?,?,?,?)",
                        (conf, team, group, int(data[conf][group][team]["for"]), int(data[conf][group][team]["against"]), data[conf][group][team]["position"],))
    conn.commit()

def main():
    cur, conn = open_database("sports.db")
    data = get_basketball_data()
    make_basketball_table(data, cur, conn)
    
if __name__ == "__main__":
    main()