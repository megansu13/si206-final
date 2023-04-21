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
    response = requests.get(url, headers=headers)
    leagues = response.json()
    id = leagues["response"][0]["id"]
    # NBA
    leagueName = leagues["response"][0]["name"]
    url2 = f"https://v1.basketball.api-sports.io/standings?league={id}&season=2019-2020"
    response2 = requests.get(url2, headers=headers)
    standings = response2.json()
    # print(standings)
    standings_dict = {}
    standings_dict[leagueName] = {}
    for i in range(len(standings["response"][0])):
        position = standings['response'][0][i]['position']
        teamName = standings['response'][0][i]['team']['name']
        forPoints = standings['response'][0][i]['points']['for']
        against = standings['response'][0][i]['points']['against']
        leagueID = standings['response'][0][i]['league']['id']
        if standings['response'][0][i]['group']['name'] == "Eastern Conference":
            if "Eastern Conference" not in standings_dict[leagueName]:
                standings_dict[leagueName]["Eastern Conference"] = {}
            
            standings_dict[leagueName]["Eastern Conference"][teamName] = {}
            standings_dict[leagueName]["Eastern Conference"][teamName]["position"] = position 
            standings_dict[leagueName]["Eastern Conference"][teamName]["for"] = forPoints
            standings_dict[leagueName]["Eastern Conference"][teamName]['id'] = leagueID
            standings_dict[leagueName]["Eastern Conference"][teamName]["against"] = against
        elif standings['response'][0][i]['group']['name'] == "Atlantic":
            if "Atlantic" not in standings_dict[leagueName]:
                standings_dict[leagueName]["Atlantic"] = {}

            standings_dict[leagueName]["Atlantic"][teamName] = {}
            standings_dict[leagueName]["Atlantic"][teamName]["position"] = position 
            standings_dict[leagueName]["Atlantic"][teamName]["for"] = forPoints
            standings_dict[leagueName]["Atlantic"][teamName]['id'] = leagueID
            standings_dict[leagueName]["Atlantic"][teamName]["against"] = against
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
    # print(data)
    make_basketball_table(data, cur, conn)
    
if __name__ == "__main__":
    main()