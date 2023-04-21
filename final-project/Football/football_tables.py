# Your name: Gunhaar Panjwani
# Your student id: 32587003
# Your email: gunhaar@umich.edu
# List who you have worked with on this project: Megan Su and Vasundhara Kulkarni
import os
import sqlite3
import requests

# For Football Sports KEY: 8083a405acmsh6a6520e04afa316p171d36jsn6bd22ce85d62
# IMPORTANT NOTE:

def open_database(db_name):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def get_prem_data(cur, conn):
    url = "https://soccer-football-info.p.rapidapi.com/championships/list/"
    querystring = {"c":"GB","l":"en_US"}
    headers = {
        "X-RapidAPI-Key": "8083a405acmsh6a6520e04afa316p171d36jsn6bd22ce85d62",
        "X-RapidAPI-Host": "soccer-football-info.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    leagues = response.json()
    id = ""
    for league in leagues["result"]:
        if league["name"] == "England Premier League":
            id = league["id"]
            id_int = ''.join([str(ord(char)) for char in id])
            mod_val = 10 ** 3
            id_int = int(id_int) % mod_val
    cur.execute("INSERT OR IGNORE INTO Football_Leagues (id, league, league_id) VALUES (?,?,?)",
                (id_int, "Premier League", id,))
    conn.commit()

def get_bundes_data(cur, conn):
    url = "https://soccer-football-info.p.rapidapi.com/championships/list/"
    querystring = {"c":"DE","l":"en_US"}
    headers = {
        "X-RapidAPI-Key": "8083a405acmsh6a6520e04afa316p171d36jsn6bd22ce85d62",
        "X-RapidAPI-Host": "soccer-football-info.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    leagues = response.json()
    id = ""
    for league in leagues["result"]:
        if league["name"] == "Germany Bundesliga I":
            id = league["id"]
            id_int = ''.join([str(ord(char)) for char in id])
            mod_val = 10 ** 3
            id_int = int(id_int) % mod_val
    cur.execute("INSERT OR IGNORE INTO Football_Leagues (id, league, league_id) VALUES (?,?,?)",
                (id_int, "Bundesliga", id,))
    conn.commit()

def get_french_data(cur, conn):
    url = "https://soccer-football-info.p.rapidapi.com/championships/list/"
    querystring = {"c":"FR","l":"en_US"}
    headers = {
        "X-RapidAPI-Key": "8083a405acmsh6a6520e04afa316p171d36jsn6bd22ce85d62",
        "X-RapidAPI-Host": "soccer-football-info.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    leagues = response.json()
    id = ""
    for league in leagues["result"]:
        if league["name"] == "France Ligue 1":
            id = league["id"]
            id_int = ''.join([str(ord(char)) for char in id])
            mod_val = 10 ** 3
            id_int = int(id_int) % mod_val
    cur.execute("INSERT OR IGNORE INTO Football_Leagues (id, league, league_id) VALUES (?,?,?)",
                (id_int, "Ligue 1", id,))
    conn.commit()

def get_spanish_data(cur, conn):
    url = "https://soccer-football-info.p.rapidapi.com/championships/list/"
    querystring = {"c":"ES","l":"en_US"}
    headers = {
        "X-RapidAPI-Key": "8083a405acmsh6a6520e04afa316p171d36jsn6bd22ce85d62",
        "X-RapidAPI-Host": "soccer-football-info.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    leagues = response.json()
    id = ""
    for league in leagues["result"]:
        if league["name"] == "Spain Primera Liga":
            id = league["id"]
            id_int = ''.join([str(ord(char)) for char in id])
            mod_val = 10 ** 3
            id_int = int(id_int) % mod_val
    cur.execute("INSERT OR IGNORE INTO Football_Leagues (id, league, league_id) VALUES (?,?,?)",
                (id_int, "LaLiga", id,))
    conn.commit()

def get_italian_data(cur, conn):
    url = "https://soccer-football-info.p.rapidapi.com/championships/list/"
    querystring = {"c":"IT","l":"en_US"}
    headers = {
        "X-RapidAPI-Key": "8083a405acmsh6a6520e04afa316p171d36jsn6bd22ce85d62",
        "X-RapidAPI-Host": "soccer-football-info.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    leagues = response.json()
    id = ""
    for league in leagues["result"]:
        if league["name"] == "Italy Serie A":
            id = league["id"]
            id_int = ''.join([str(ord(char)) for char in id])
            mod_val = 10 ** 3
            id_int = int(id_int) % mod_val
    cur.execute("INSERT OR IGNORE INTO Football_Leagues (id, league, league_id) VALUES (?,?,?)",
                (id_int, "Serie A", id,))
    conn.commit()

def get_dutch_data(cur, conn):
    url = "https://soccer-football-info.p.rapidapi.com/championships/list/"
    querystring = {"c":"NL","l":"en_US"}
    headers = {
        "X-RapidAPI-Key": "8083a405acmsh6a6520e04afa316p171d36jsn6bd22ce85d62",
        "X-RapidAPI-Host": "soccer-football-info.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    leagues = response.json()
    id = ""
    for league in leagues["result"]:
        if league["name"] == "Netherlands Eredivisie":
            id = league["id"]
            id_int = ''.join([str(ord(char)) for char in id])
            mod_val = 10 ** 3
            id_int = int(id_int) % mod_val
    cur.execute("INSERT OR IGNORE INTO Football_Leagues (id, league, league_id) VALUES (?,?,?)",
                (id_int, "Eredivisie", id,))
    conn.commit()

# need points scored per team and final standing for 5 seasons
def make_football_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Football_Leagues (id INTEGER PRIMARY KEY, "
                "league TEXT, league_id TEXT UNIQUE)")
    conn.commit()

def main():
    cur, conn = open_database("sports.db")
    make_football_table(cur, conn)
    get_prem_data(cur, conn)
    get_bundes_data(cur, conn)
    get_french_data(cur, conn)
    get_italian_data(cur, conn)
    get_spanish_data(cur, conn)
    get_dutch_data(cur, conn)

if __name__ == "__main__":
    main()
