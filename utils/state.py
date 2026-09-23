from langgraph.graph import StateGraph,MessagesState 
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv find_dotenv 
from langchain.messages import SystsemMessage 
from typing import Literal


class state(MessagesState):
    count:int
builder=StateGraph(MessageState)

