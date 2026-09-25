from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END,MessagesState
from langchain.tools import tool 
from dotenv import load_dotenv,find_dotenv 
from sqlalchemy import create_engine,text
#Load our env variables:
_=load_dotenv(find_dotenv())
#We start by isntanciating our model object:
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
#We create our sqlalchemy engine:
engine=create_engine("sqlite:///agent.db")
#Retrieve our prompts in our script :
with open("text_to_query_prompt.md","r",encoding="utf-8") as f :
    text_to_query_prompt=f.read()

def text_to_query(state:MessagesState)->MessagesState:
    """
    This function will take user input and make it into a  SQL query!
    """
    query=model.invoke([text_to_query_prompt]+state["messages"])
    return {"messages":state["messages"]+[query.content]}
@tool 
def execute_query(state:MessagesState,engine){
    """
    This function will take our query and execute it using sqlalchemy
    """
with engine.conect() as conn :
#We execute the llms reply which will be our sql query :
    result=conn.execute(text(state["messages"][-1]))
    rows=result.fetchall()
    return {"messages":state["messages"]+rows}
}
model_with_tools=model.bind_tools([execute_query])
builder=StateGraph(MessagesState)
builder.add_node("text_to_query",text_to_query)
builder.add_node("execute_query",execute_query)
builder.add_edge(START,"text_to_query")
builder.add_edge("text_to_query","execute_query")
builder.add_edge("execute_query",END)
graph=builder.compile()
