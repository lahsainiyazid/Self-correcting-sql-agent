from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END,MessagesState
from langchain_core.messages import AIMessage
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
with open("query_to_text_prompt.md","r",encoding="utf-8") as f:
    query_to_text_prompt=f.read()
def text_to_query(state:MessagesState)->MessagesState:
    """
    This function will take user input and make it into a  SQL query!
    """
    query=model.invoke([text_to_query_prompt]+state["messages"])
    return {"messages":[query.content]}
def execute_query(state:MessagesState):
    """
    This function will take our query and execute it using sqlalchemy
    """
    last_message=state["messages"][-1]
    sql_string=last_message.content 
    with engine.connect() as conn :
#We execute the llms reply which will be our sql query :
        result=conn.execute(text(sql_string)) #sqlalchemy does not allow us to pass raw strings.
        rows=result.fetchall()
    return {"messages":[AIMessage(content=str(rows))]}

def query_to_text(state:MessagesState):
    """
    This function will take our query result  and turn it into human readable format!
    """
    query_result=state["messages"][-1]
    query_string=query_result.content
    llm_response=model.invoke(query_string)
    return {"messages":llm_response}



builder=StateGraph(MessagesState)
builder.add_node("text_to_query",text_to_query)
builder.add_node("execute_query",execute_query)
builder.add_node("query_to_text",query_to_text)
builder.add_edge(START,"text_to_query")
builder.add_edge("text_to_query","execute_query")
builder.add_edge("execute_query","query_to_text")
builder.add_edge("query_to_text",END)
graph=builder.compile()
