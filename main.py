from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,Start,END
from dotenv import load_dotenv,find_dotenv 
_=load_dotenv(find_dotenv())
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
