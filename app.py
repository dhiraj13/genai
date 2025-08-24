# New import for the Gemini model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# New model instantiation
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

message = HumanMessage(
    content="What is the difference between a galaxy and a nebula?")

response = llm.invoke([message])

print(response.content)
