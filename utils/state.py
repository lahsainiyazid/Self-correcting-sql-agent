from langgraph.graph import StateGraph,MessageState 
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv find_dotenv 
from langchain.messages import SystsemMessage 
from typing import Literal


builder=StateGraph(MessageState)

