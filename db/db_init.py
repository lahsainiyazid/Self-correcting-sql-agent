import sqlite3 

class init():
    def __init__db():
        conn=sqlite3.connect("agent.db")
        curr=conn.cursor()
        curr.execute("CREATE TABLE IF NOT EXISTS movies(title,year,score,director,country)")
 
