from pydantic import BaseModel,Field #Field allows us to add constraints to our fields in pydantic 
from typing import List 
#Creating our own class(object analyst):
class Analyst(BaseModel):
    affiliation:str=Field(description="Primary affiliation of the analyst")
    name:str=Field(description="Name of the analyst")
    role:str=Field(description="role of the analyst in the context of the topic.")
    description:str=Field(description="Description of the analyst focus,concerns,and motives")
    @property #Python decorator that transformes a method into a getter: 
    def persona(self)->str:
        return f"Name:{self.name}\nRole:{self.role}\nAffiliation:{self.affiliation}\Description:{self.description}"

class Perspective(BaseModel):
    analysts:List[Analyst]=Field(description="Comprehensive list of analysts with their roles and affiliations")






