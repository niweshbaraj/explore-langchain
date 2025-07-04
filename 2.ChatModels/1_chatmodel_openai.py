from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# model = ChatOpenAI(model='gpt-4')
model = ChatOpenAI(model='gpt-4', temperature=0.7)

result = model.invoke("What is the capital of India")

model = ChatOpenAI(model='gpt-4', temperature=1.5)
result = model.invoke("Write a 5 line poem on cricket")

model = ChatOpenAI(model='gpt-4', temperature=0.7, max_completion_tokens=10)
result = model.invoke("Write a 5 line poem on cricket")

# print(result)
print(result.content)

# DON'T HAVE OPENAI CREDIT TO RUN THE ABOVE CONTENT