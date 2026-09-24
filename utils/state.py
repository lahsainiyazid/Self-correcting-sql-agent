from langgraph.graph import StateGraph,MessagesState 
from langchain.messages import SystemMessage 
from typing import Literal


class state(MessagesState):
    count:int
builder=StateGraph(MessagesState)

