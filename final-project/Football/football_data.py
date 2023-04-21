# Your name: Gunhaar Panjwani
# Your student id: 32587003
# Your email: gunhaar@umich.edu
# List who you have worked with on this project: Megan Su and Vasundhara Kulkarni

import os
import sqlite3
import matplotlib
import matplotlib.pyplot as plt


def open_database(db_name):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


def process_pl(cur, conn):
    cur.execute("SELECT team, position, for, against FROM Football JOIN Football_Leagues "
                "ON Football.league = Football_Leagues.id "
                "WHERE Football_Leagues.league = 'Premier League'")
    ret_list = cur.fetchall()
    pos_list = []
    gd_list = []
    for i in range(len(ret_list)):
        pos_list.append(ret_list[i][1])
        gd_list.append(ret_list[i][2] - ret_list[i][3])
    return (pos_list, gd_list)


def process_bl(cur, conn):
    cur.execute("SELECT team, position, for, against FROM Football JOIN Football_Leagues "
                "ON Football.league = Football_Leagues.id "
                "WHERE Football_Leagues.league = 'Bundesliga'")
    ret_list = cur.fetchall()
    pos_list = []
    gd_list = []
    for i in range(len(ret_list)):
        pos_list.append(ret_list[i][1])
        gd_list.append(ret_list[i][2] - ret_list[i][3])
    return (pos_list, gd_list)


def process_sa(cur, conn):
    cur.execute("SELECT team, position, for, against FROM Football JOIN Football_Leagues "
                "ON Football.league = Football_Leagues.id "
                "WHERE Football_Leagues.league = 'Serie A'")
    ret_list = cur.fetchall()
    pos_list = []
    gd_list = []
    for i in range(len(ret_list)):
        pos_list.append(ret_list[i][1])
        gd_list.append(ret_list[i][2] - ret_list[i][3])
    return (pos_list, gd_list)


def process_l1(cur, conn):
    cur.execute("SELECT team, position, for, against FROM Football JOIN Football_Leagues "
                "ON Football.league = Football_Leagues.id "
                "WHERE Football_Leagues.league = 'Ligue 1'")
    ret_list = cur.fetchall()
    pos_list = []
    gd_list = []
    for i in range(len(ret_list)):
        pos_list.append(ret_list[i][1])
        gd_list.append(ret_list[i][2] - ret_list[i][3])
    return (pos_list, gd_list)


def process_ed(cur, conn):
    cur.execute("SELECT team, position, for, against FROM Football JOIN Football_Leagues "
                "ON Football.league = Football_Leagues.id "
                "WHERE Football_Leagues.league = 'Eredivisie'")
    ret_list = cur.fetchall()
    pos_list = []
    gd_list = []
    for i in range(len(ret_list)):
        pos_list.append(ret_list[i][1])
        gd_list.append(ret_list[i][2] - ret_list[i][3])
    return (pos_list, gd_list)


def process_ll(cur, conn):
    cur.execute("SELECT team, position, for, against FROM Football JOIN Football_Leagues "
                "ON Football.league = Football_Leagues.id "
                "WHERE Football_Leagues.league = 'LaLiga'")
    ret_list = cur.fetchall()
    pos_list = []
    gd_list = []
    for i in range(len(ret_list)):
        pos_list.append(ret_list[i][1])
        gd_list.append(ret_list[i][2] - ret_list[i][3])
    return (pos_list, gd_list)


def drawPLData(data):
    fig, ax = plt.subplots()
    ax.plot(data[1], data[0], "bo-", label="Premier League")
    ax.legend()
    ax.set_xlabel("Goal Difference")
    ax.set_ylabel("Position")
    ax.set_title("Goal Difference vs Position in Premier League 20/21 Season")
    ax.grid()
    ax.set_yticks(range(0, 21, 1))
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "Football_PL.png")
    fig.savefig(full_path)


def drawBundesligaData(data):
    fig, ax = plt.subplots()
    ax.plot(data[1], data[0], "ro-", label="Bundesliga")
    ax.legend()
    ax.set_xlabel("Goal Difference")
    ax.set_ylabel("Position")
    ax.set_title("Goal Difference vs Position in Bundesliga 20/21 Season")
    ax.grid()
    ax.set_yticks(range(0, 19, 1))
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "Football_BL.png")
    fig.savefig(full_path)


def drawLaLigaData(data):
    fig, ax = plt.subplots()
    ax.plot(data[1], data[0], "yo-", label="LaLiga")
    ax.legend()
    ax.set_xlabel("Goal Difference")
    ax.set_ylabel("Position")
    ax.set_title("Goal Difference vs Position in LaLiga 20/21 Season")
    ax.grid()
    ax.set_yticks(range(0, 21, 1))
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "Football_LL.png")
    fig.savefig(full_path)


def drawSerieAData(data):
    fig, ax = plt.subplots()
    ax.plot(data[1], data[0], "go-", label="Serie A")
    ax.legend()
    ax.set_xlabel("Goal Difference")
    ax.set_ylabel("Position")
    ax.set_title("Goal Difference vs Position in Serie A 20/21 Season")
    ax.grid()
    ax.set_yticks(range(0, 21, 1))
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "Football_SA.png")
    fig.savefig(full_path)


def drawEredivisieData(data):
    fig, ax = plt.subplots()
    ax.plot(data[1], data[0], "co-", label="Eredivisie")
    ax.legend()
    ax.set_xlabel("Goal Difference")
    ax.set_ylabel("Position")
    ax.set_title("Goal Difference vs Position in Eredivisie 20/21 Season")
    ax.grid()
    ax.set_yticks(range(0, 19, 1))
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "Football_ED.png")
    fig.savefig(full_path)


def drawLigue1Data(data):
    fig, ax = plt.subplots()
    ax.plot(data[1], data[0], "mo-", label="Ligue 1")
    ax.legend()
    ax.set_xlabel("Goal Difference")
    ax.set_ylabel("Position")
    ax.set_title("Goal Difference vs Position in Ligue 1 20/21 Season")
    ax.grid()
    ax.set_yticks(range(0, 21, 1))
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "Football_L1.png")
    fig.savefig(full_path)


def print_to_file(pl_data, bd_data, ll_data, sa_data, l1_data, ed_data):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "football.txt")
    with open(full_path, "w") as f:
        f.write("Calculation: Goal Difference = Goals For - Goals Against\n")
        f.write("\n")
        f.write("Premier League Data:\n")
        f.write(f"Goal Difference: {pl_data[1]}\n")
        f.write(f"Position: {pl_data[0]}\n")
        f.write("\n")
        f.write("Bundesliga Data:\n")
        f.write(f"Goal Difference: {bd_data[1]}\n")
        f.write(f"Position: {bd_data[0]}\n")
        f.write("\n")
        f.write("LaLiga Data:\n")
        f.write(f"Goal Difference: {ll_data[1]}\n")
        f.write(f"Position: {ll_data[0]}\n")
        f.write("\n")
        f.write("Serie A Data:\n")
        f.write(f"Goal Difference: {sa_data[1]}\n")
        f.write(f"Position: {sa_data[0]}\n")
        f.write("\n")
        f.write("Ligue 1 Data:\n")
        f.write(f"Goal Difference: {l1_data[1]}\n")
        f.write(f"Position: {l1_data[0]}\n")
        f.write("\n")
        f.write("Eredivisie Data:\n")
        f.write(f"Goal Difference: {ed_data[1]}\n")
        f.write(f"Position: {ed_data[0]}\n")


def main():
    cur, conn = open_database("sports.db")
    pl_data = process_pl(cur, conn)
    bd_data = process_bl(cur, conn)
    ll_data = process_ll(cur, conn)
    sa_data = process_sa(cur, conn)
    l1_data = process_l1(cur, conn)
    ed_data = process_ed(cur, conn)
    print_to_file(pl_data, bd_data, ll_data, sa_data, l1_data, ed_data)
    drawPLData(pl_data)
    drawEredivisieData(ed_data)
    drawBundesligaData(bd_data)
    drawLaLigaData(ll_data)
    drawSerieAData(sa_data)
    drawLigue1Data(l1_data)
    plt.show()


if __name__ == "__main__":
    main()
