from openai import Client
from dotenv import load_dotenv
import os

load_dotenv()

#Gerenciador do client da openAI
class OpenAI_Client():
    def __init__(self):
        self.OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
        self.OPENAI_ASSISTANT_ID=os.getenv("OPENAI_ASSISTANT_ID")
        self.VECTOR_STORE_ID=os.getenv("VECTOR_STORE_ID")
        self.client = Client(api_key=self.OPENAI_API_KEY)