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


def get_football_data(cur, conn):
    id, qid = cur.execute(
        "SELECT id, league_id FROM Football_Leagues WHERE league = 'Serie A'").fetchone()
    url = "https://soccer-football-info.p.rapidapi.com/championships/view/"
    querystring = {"i": qid, "l": "en_US"}
    headers = {
        "X-RapidAPI-Key": "8083a405acmsh6a6520e04afa316p171d36jsn6bd22ce85d62",
        "X-RapidAPI-Host": "soccer-football-info.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    # 20/21 season
    league_info = response.json()["result"][0]["seasons"][0]
    standings_dict = {}
    for i in range(len(league_info["groups"][0]["table"])):
        name = league_info["groups"][0]["table"][i]["team"]["name"]
        standings_dict[name] = {}
        standings_dict[name]["id"] = league_info["groups"][0]["table"][i]["team"]["id"]
        standings_dict[name]["position"] = league_info["groups"][0]["table"][i]["position"]
        standings_dict[name]["for"] = league_info["groups"][0]["table"][i]["goals_scored"]
        standings_dict[name]["against"] = league_info["groups"][0]["table"][i]["goals_conceded"]
        standings_dict[name]["league"] = id
    return standings_dict

# need points scored per team and final standing for 5 seasons
def make_football_table(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Football (id TEXT PRIMARY KEY, "
                "league TEXT, team TEXT, position INTEGER, for INTEGER, against INTEGER)")
    for team in data:
        cur.execute("INSERT OR IGNORE INTO Football (id, league, team, for, against, position) VALUES (?,?,?,?,?,?)",
                    (data[team]["id"], data[team]["league"], team, int(data[team]["for"]),
                     int(data[team]["against"]), data[team]["position"],))
    conn.commit()



def main():
    cur, conn = open_database("sports.db")
    data = get_football_data(cur, conn)
    make_football_table(data, cur, conn)


if __name__ == "__main__":
    main()
