from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Obter documentos
files = [".\data\\" + filepath for filepath in os.listdir('.\data') if filepath.endswith((".pdf", ".txt"))]

# Criar um vector store chamado "consortium_laws"
vector_store = client.beta.vector_stores.create(name="consortium_laws")

# Preparar os arquivos para upload no OpenAI
file_streams = [open(path, "rb") for path in files]

# Adiciona os arquivos ao vector store,
# e verifica o status do lote de arquivos até a conclusão.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

# Imprimir o status e a contagem de arquivos do lote para ver o resultado desta operação.
print(file_batch.status)
print(file_batch.file_counts)
