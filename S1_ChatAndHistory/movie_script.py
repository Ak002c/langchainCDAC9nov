import os
import configparser

from langchain_groq import ChatGroq
from langchain_cohere import ChatCohere

from langchain_core.messages import HumanMessage, SystemMessage

config = configparser.ConfigParser()
config.read('../config.ini')

groq = config['groq']
cohere = config['cohere']

os.environ['GROQ_API_KEY'] = groq.get('GROQ_API_KEY')
os.environ['COHERE_API_KEY'] = cohere.get('COHERE_API_KEY')

messages = [
    SystemMessage(content='You are a weather service. You will respond to weather queries to the best of you ability. You will always end with - Have a great day'),
    HumanMessage(content='Hey whats the weather like today?')
]

model = ChatGroq(model="llama3-8b-8192")
print(model.invoke(messages))