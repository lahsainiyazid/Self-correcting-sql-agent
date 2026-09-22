from dotenv import load_dotenv find_dotenv
from states import GenerateAnalystsState
from models import llm 
from objects import Analyst,Perspectives
from prompts import analyst_instructions
_=load_dotenv(find_dotenv())
#nodes:
def create_analysts(state:GenerateAnalystsState):
    """
    Create analysts 
    """ 
    topic=state["topic"]
    max_analysts=state["max_analysts"]
    human_feedback=state.get("human_analyst_feedback","")
    #Enforce structured output :
    structured_llm=llm.structured_output()
    #system_message:
    system_message=
    pass 

