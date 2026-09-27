from state import AgentState
from llm import model 
from engine import engine
from prompts import text_to_query_prompt,query_to_text_prompt
from langchain_core.messages import AIMessage
from sqlalchemy import text,inspect
def text_to_query(state:AgentState)->AgentState:
    """
    This function will take user input and make it into a  SQL query!
    """
    query=model.invoke([text_to_query_prompt]+state["messages"])
    return {"messages":[AIMessage(query.content)],
            "retry_count":state.get("retry_count",0),
            "error":state.get("Error")}
def execute_query(state:AgentState):
    """
    This function will take our query and execute it using sqlalchemy
    """
    last_message=state["messages"][-1]
    sql_string=last_message.content 
    try:
        with engine.connect() as conn :
#We execute the llms reply which will be our sql query :
            result=conn.execute(text(sql_string)) #sqlalchemy does not allow us to pass raw strings.
            rows=result.fetchall()
        return {"messages":[AIMessage(content=str(rows))],
            "retry_count":state.get("retry_count")+1}
    except Exception as e:
        return {
            "messages":[AIMessage(content=f"Query Failed:{e}")],
            "retry_count":state.get("retry_count",0)+1,
            "error":str(e)
        }


def query_to_text(state:AgentState):
    """
    This function will take our query result  and turn it into human readable format!
    """
    query_result=state["messages"][-1]
    query_string=query_result.content
    llm_response=model.invoke(query_string)
    return {"messages":llm_response}

def check_too_many_retries(state:AgentState):
    if (state.get("error") is not None):
        if (state.get("retry_count")>=3):
            return END 
        else:
            return "text_to_query"
    else:
        return "query_to_text"

