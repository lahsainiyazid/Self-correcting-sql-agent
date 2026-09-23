from model import model 
from state import builder
from langgraph.graph import START,END 
from langchain.tools import tool 
from langchain.prebuilt import ToolNode,tools_condition
from dotenv import load_dotenv,find_dotenv
from propmts import system_message_prompt,system_message_query
from typing import Literal
from state import state,builder  
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
@tool 
def verify_query():
def count(state:state)->Literal[END,execute_query]:
    if state["count"]>3:
        return END
    else:
        return execute_query


#We import our model and add to it tools:
model_with_tools=model.bind_tools([execute_query,verify_query])
#We import our builder and add nodes:
builder.add_node("execute_query",execute_query)
builder.add_node("text_to_query",text_to_query)
builder.add_node("verify_query",verify_query)
builder.add_node("is_new_query",is_new_query)
graph=builder.compile() 
