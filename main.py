from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END,MessagesState
from langchain.tools import tool 
from dotenv import load_dotenv,find_dotenv 
#Load our env variables:
_=load_dotenv(find_dotenv())
#We start by isntanciating our model object:
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
#Retrieve our prompts in our script :
with open("text_to_query_prompt.md","r",encoding="utf-8") as f :
    text_to_query_prompt=f.read()

def text_to_query(state:MessagesState)->MessagesState:
    """
    This function will take user input and make it into a  SQL query!
    """
    query=model.invoke([text_to_query_prompt]+state["messages"])
    return {"messages":state["messages"]+[query.content]}
builder=StateGraph(MessagesState)
builder.add_node("text_to_query",text_to_query)
builder.add_edge(START,"text_to_query")
builder.add_edge("text_to_query",END)
graph=builder.compile()
