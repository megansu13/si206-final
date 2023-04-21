# Your name: Vasundhara Kulkarni
# Your student id: 01211840
# Your email: kulkvasu@umich.edu
# List who you have worked with on this project: Gunhaar Panjwani and Megan Su

import sqlite3
import os
import matplotlib.pyplot as plt

def open_database(db_name):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def getData(cur, conn):
    cur.execute("SELECT conference, name, forPoints, againstPoints, (forPoints - againstPoints) AS pointDifferential FROM Basketball")
    data = {}
    for row in cur.fetchall():
        if row[0] not in data:
            data[row[0]] = {row[1]:[row[4]]}
        else:
            if row[1] not in data[row[0]]:
                data[row[0]][row[1]] = [row[4]]
            else:
                data[row[0]][row[1]].append(row[4])
    conn.close()
    return data

def printToFile(data):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "dataResults.txt")
    with open(full_path, "w") as f:
        f.write("Calculation: Point Difference = Points For - Points Against\n")
        f.write("\n")
        for conference in data:
            f.write(f"{conference}:\n")
            for team in sorted(data[conference], key=lambda x: sum(data[conference][x]), reverse=True):
                f.write(f"{team}: {data[conference][team]}\n")
                positions = range(len(data[conference][team]))
                f.write(f"Position: {[p + 1 for p in positions]}\n\n")

def plot_data(data):
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'gray']
    i = 0
    for conference in data:
        for league in data[conference]:
            if conference != 'NBA':
                plt.plot(data[conference][league], range(len(data[conference][league])), color = colors[i],label=league, marker='o')
            else:
                plt.plot(data[conference][league], range(len(data[conference][league])),label=league, marker='o')
        plt.legend()
        plt.grid()
        plt.title(f"{conference}: Total Points vs Position")
        plt.xlabel("Total Points")
        plt.ylabel("Position")
        base_path = os.path.abspath(os.path.dirname(__file__))
        full_path = os.path.join(base_path, f"{conference}.png")
        plt.savefig(full_path)
        plt.show()
        i+=1

def main():
    cur, conn = open_database("sports.db")
    data = getData(cur, conn)
    printToFile(data)
    plot_data(data)

if __name__ == '__main__':
    main()
