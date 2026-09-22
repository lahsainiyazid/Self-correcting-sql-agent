from typing_extensions import TypedDict ,NotRequired
from typing import Optional
from objects import Analyst 


#State 
class GenerateAnalystsState(TypedDict):
    topic:str #Research topic 
    max_analysts:int #Number of analysts 
    #Human feedback to the llm .
    human_analytst_feedback:NotRequired[Optional] #Not required key must be omitted and optional :if exists value can be null 
    analysts:NotRequired[List[analysts]] #List of all our analysts 


