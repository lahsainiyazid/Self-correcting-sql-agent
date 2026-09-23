from model import model 
from state import builder
from langgraph.graph import START,END 
from langchain.tools import tool 
from langchain.prebuilt import ToolNode,tools_condition
from dotenv import load_env find_env
_=load_env(find_env)




@tool 
def text_to_query():
@tool 
def execute_query():
@tool 
def verify_query():
    
@tool 
def count():
    if state["count"]>3:
        return END
    else:
        return execute_query


#We import our model and add to it tools:
model_with_tools=model.bind_tools([text_to_query,execute_query,verify_query,count])
#We import our builder and add nodes:
builder.add_node()
builder.add_node()
builder.add_node()
graph=builder.compile()
