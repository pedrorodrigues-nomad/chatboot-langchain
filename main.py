import os

api_key = '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'

os.environ['GROQ_API_KEY'] = api_key

from langchain_groq import ChatGroq


chat = ChatGroq(model='llama-3.3-70b-versatile')

response = chat.invoke('Hello world! How are you ?')

print(response)

