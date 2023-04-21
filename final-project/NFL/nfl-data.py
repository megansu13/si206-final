# Your name: Megan Su
# Your student id: 76790483
# Your email: meganysu@umich.edu
# List who you have worked with on this project: Gunhaar Panjwani and Vasundhara Kulkarni

import sqlite3
import matplotlib.pyplot as plt
import os

def getData():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    conn = sqlite3.connect(path+'/'+"sports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT season, division, name, wins, losses, for, against FROM NFL")
    data = {}
    points = {}
    for row in cursor.fetchall():
        if row[0] not in data:
            data[row[0]] = {row[1]:[round(row[3] / (row[3] + row[4]),3)]}
            points[row[0]] = {row[1]:[row[5] - row[6]]}
        else:
            if row[1] not in data[row[0]]:
                data[row[0]][row[1]] = [round(row[3] / (row[3] + row[4]),3)]
            else:
                data[row[0]][row[1]].append(round(row[3] / (row[3] + row[4]),3))
            if row[1] not in points[row[0]]:
                points[row[0]][row[1]] = [row[5] - row[6]]
            else:
                points[row[0]][row[1]].append(row[5] - row[6])
    conn.close()
    return data, points

def file(data, points):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "nfl-results.txt")
    with open(full_path, "w") as f:
        f.write(f"Calculation: Win Percentage = Wins / (Wins + Losses) and Net Points = For Points - Against Points\n")
        f.write("\n")
        for season in data:
            f.write(f"{season}:\n")
            for div in data[season]:
                f.write(f"{div}\n")
                f.write(f"Win Percentage: {data[season][div]}\n")
                f.write(f"Net Points: {points[season][div]}\n\n")
        

def plot(data,points):
    for season in data:
        for div in data[season]:
            plt.plot(points[season][div], data[season][div], label=div)
        plt.legend()
        plt.title(str(season)+' NFL Net Points vs. Win Percentage')
        plt.grid()
        plt.xlabel("Net Points")
        plt.ylabel("Win Percentage")
        plt.show()
        base_path = os.path.abspath(os.path.dirname(__file__))
        full_path = os.path.join(base_path, "nfl-"+str(season)+".png")
        plt.savefig(full_path)

def main():
    data, points = getData()
    file(data, points)
    plot(data, points)

if __name__ == '__main__':
    main()
