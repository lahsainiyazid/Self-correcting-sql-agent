from langchain.messages import SystemMessage
with open ("./system_prompt.md","r",encoding="utf-8") as f:
    system_prompt=f.read()
    

with open("./query_prompt.md","r",encoding="utf-8") as f:
    query_prompt=f.read()


system_message_prompt=SystemMessage(content=system_prompt)
system_megssage_query=SystemMessage(content=query_prompt)


