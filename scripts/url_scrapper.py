from langchain_community.document_loaders import UnstructuredURLLoader

# Abre o arquivo que contém as URLs e lê todas as linhas
with open(r".\files\urls.txt", 'r' , encoding="utf-8") as f:
    urls = f.readlines()

# Inicializa o carregador de URLs com as URLs lidas
loader = UnstructuredURLLoader(urls=urls)

# Carrega os dados das URLs
data = loader.load()

# Obtém o nome do arquivo a partir dos metadados da primeira URL carregada
file_name = data[0].metadata.get("source").split(r"/") 

# Imprime o nome do arquivo
print(file_name[-1])

# Salva o conteúdo da página em um arquivo de texto
with open(r".\\data\\" + file_name[-2].replace("-", "_") + ".txt", 'w', encoding="utf8") as f:
    f.write(data[0].page_content)
