from dotenv import load_dotenv
import os
from .openai_client import OpenAI_Client
import json

load_dotenv()

#Classe para gerenciar as threads
class ThreadsChat(OpenAI_Client):
    def __init__(self):
        super().__init__()
        self.threads = self.client.beta.threads
        self.threads_list = self.get_threads()

    # Função para criar threads
    def create(self):
        thread_obj = self.threads.create(
            tool_resources={
                "file_search": 
                    {"vector_store_ids": [self.VECTOR_STORE_ID]}}
        )

        if thread_obj:
            # Salva o ID da thread criada em um arquivo
            with open(r".\files\threads.txt", 'a+') as f:
                f.write(thread_obj.id + "\n")
        return thread_obj 
    
    @staticmethod
    def get_threads():
        # Lê os IDs das threads salvas no arquivo
        with open(r".\files\threads.txt", 'r') as f:
            threads_ids = [thread.replace("\n","") for thread in f.readlines()]
        return threads_ids
    
    def get_messages_from_thread_id(self, thread_id):
        # Lista as mensagens da thread
        thread_messages = self.threads.messages.list(thread_id)

        # Filtra as informações relevantes
        filtered_messages = [
            {
                "role": message.role,
                "content": message.content[0].text.value  # Acessa o conteúdo da mensagem
            }
            for message in thread_messages.data
        ]

        # Retorna as mensagens filtradas
        return filtered_messages
