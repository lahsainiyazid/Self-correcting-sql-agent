from pathlib import Path 
from langchain.messages import SystemMessage
UTILS_DIR=Path(__file__).parent 
PROMPT_PATH=UTILS_DIR/"system_prompt.md"
QUERY_PATH=UTILS_DIR/"query_prompt.md"
with open (PROMPT_PATH,"r",encoding="utf-8") as f:
    system_prompt=f.read()
    

with open(QUERY_PATH,"r",encoding="utf-8") as f:
    query_prompt=f.read()


system_message_prompt=SystemMessage(content=system_prompt)
system_megssage_query=SystemMessage(content=query_prompt)


