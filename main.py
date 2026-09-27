from langgraph.graph import StateGraph,START,END 
from dotenv import load_dotenv,find_dotenv 
from state import AgentState
from functions import text_to_query,execute_query,query_to_text,check_too_many_retries
#Load our env variables:
_=load_dotenv(find_dotenv())

builder=StateGraph(AgentState)
builder.add_node("text_to_query",text_to_query)
builder.add_node("execute_query",execute_query)
builder.add_node("query_to_text",query_to_text)
builder.add_edge(START,"text_to_query")
builder.add_edge("text_to_query","execute_query")
builder.add_conditional_edges("execute_query",check_too_many_retries,{"text_to_query":"text_to_query",   #We map each output of our primary function to node 
                                                                      "query_to_text":"query_to_text",
                                                                      END:END})
builder.add_edge("query_to_text",END)
graph=builder.compile()
