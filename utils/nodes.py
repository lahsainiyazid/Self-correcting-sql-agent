from langgraph.graph import START,END 
from langchain.tools import tool 
from langgraph.prebuilt import ToolNode,tools_condition
from dotenv import load_dotenv,find_dotenv
from typing import Literal 
from utils.prompts import system_message_prompt,system_message_query
from utils.state import state,builder
from utils.model import model
from sql_alchemy import engine 
_=load_env(find_env)
def text_to_query(state:state)->state:
    """
    This tool transforms the user's text into a sql query to execute!
    """
    return {
       model.invoke(state["messages"]+state[system_message_prompt])
    }
    
@tool 
def execute_query():
    """
    This tool executes the sql query:
    """
    results=engine.execute_query(text(state["messages"]+state[system_message_prompt]))
    for row in results.fetchall:
        print(result)
def count(state:state)->Literal[END,execute_query]:
    if state["count"]>3:
        return END 
    else:
        return execute_query


#We import our model and add to it tools:
model_with_tools=model.bind_tools([execute_query,verify_query])
#We import our builder and add nodes:
builder.add_node("text_to_query",text_to_query)
builder.add_node("execute_query",execute_query)
#We add our edges:
builder.add_edge(START,"text_to_query")
builder.add_edge("text_to_query","execute_query")
builder.add_edge("execute_query",END)
graph=builder.compile() 
