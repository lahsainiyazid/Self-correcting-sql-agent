import sqlite3 
with sqlite3.connect("agent.db") as conn:
    curr=conn.cursor()
    curr.execute("SELECT *from  movies")
    rows=curr.fetchall()
if not rows:
    print("No rows were found!")
else :
    for row in rows:
        print(row)
