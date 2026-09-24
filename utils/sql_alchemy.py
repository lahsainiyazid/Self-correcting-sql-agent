from sqlalchemy import create_engine,text  
#We create the engine to our db 
engine=create_engine("sqlite:///../db/agent.db")
#We execute a query :
with engine.connect() as conn:
    result=conn.execute(text("select * from movies"))
    for row in result.fetchall():
        print(row)
