from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant that provides concise and accurate information."),
    HumanMessage(content="Can you explain the theory about Langchain ?"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)

