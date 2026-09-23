import sqlite3 

class dbinit():
    def __init__(self,db_name:str="agent.db"):
        self.db_name=db_name 
        self.create_table()
    def create_table(self,table_name:str="movies"):
        self.table_name=table_name 
        with sqlite3.connect(self.db_name) as conn:
            curr=conn.cursor()
            curr.execute("""CREATE TABLE IF NOT EXISTS movies 
            (title TEXT,
            year INTEGER,
            score  REAL,
            director TEXT,
            country TEXT)""")
    def insert_rows(self,movies_data:list):
        with sqlite3.connect(self.db_name) as conn:
            curr=conn.cursor()
            curr.executemany("INSERT INTO movies VALUES (?,?,?,?,?)",movies_data)

if __name__=="__main__":
    initial_movies=initial_movies = [
        ("The Shawshank Redemption", 1994, 9.3, "Frank Darabont", "USA"),
        ("The Godfather", 1972, 9.2, "Francis Ford Coppola", "USA"),
        ("Spirited Away", 2001, 8.6, "Hayao Miyazaki", "Japan"),
        ("Parasite", 2019, 8.5, "Bong Joon-ho", "South Korea"),
        ("Inception", 2010, 8.8, "Christopher Nolan", "USA"),
        ("Amélie", 2001, 8.3, "Jean-Pierre Jeunet", "France"),
        ("City of God", 2002, 8.6, "Fernando Meirelles", "Brazil"),
    ]
    db=dbinit()
    db.insert_rows(movies_data=initial_movies)


