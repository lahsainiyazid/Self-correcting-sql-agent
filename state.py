from langgraph.graph import MessagesState
class AgentState(MessagesState):
    retry_count:int=0
    error:str|None=None 

