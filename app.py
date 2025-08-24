from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-3.5-turbo")

message = HumanMessage(
    content="What is the difference between a galaxy and a nebula?")

response = llm.invoke([message])

print(response.content)
