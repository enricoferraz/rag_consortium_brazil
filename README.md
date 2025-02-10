# Especialista em Legislação de Consórcios

## Descrição

Uma aplicação Streamlit que utiliza a API da OpenAI para criar um assistente especializado em legislação de consórcios no Brasil. O assistente responde a perguntas com base em uma base de dados vetorizada, fornecendo respostas detalhadas e referenciadas.

## Índice

* Instalação
* Uso
* Configuração
* Estrutura do Projeto
* Contribuição
* Licença
* Contato

## Installation

1. Clone o repositório:

```python
git clone https://github.com/enricoferraz/rag_consortium_brazil.git
cd rag_consortium_brazil
```


2. Crie um ambiente virtual e ative-o:

```python
python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate
```


3. Instale as dependências:

```python-repl
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:

* Copie o arquivo [.env-template](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) para [.env](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) e preencha com suas credenciais da OpenAI.
* O arquivo [.env](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) deve conter:

```python
OPENAI_API_KEY="sua_chave_de_api"
OPENAI_ASSISTANT_ID="id_do_assistente"
VECTOR_STORE_ID="id_do_vector_store"
```


## Uso

1. Adicione seus arquivos PDF ou TXT na pasta [data](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html).
2. Se você tiver URLs para incluir, adicione uma por linha no arquivo [urls.txt](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html).
3. Execute o scrapper de URLs para carregar os dados das URLs:

```python
python scripts/url_scrapper.py
```

4. Crie o banco de dados vetorial e atualize o valor de `VECTOR_STORE_ID` no arquivo [.env](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html).
5. Crie o agente:

```python 
python entities/agent.py
```

6. Inicie a aplicação Streamlit:

```bash
streamlit run app.py
```

7. Acesse a aplicação no seu navegador em `http://localhost:8501`.

## Configuração

Certifique-se de que as seguintes variáveis de ambiente estão definidas no seu arquivo [.env](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html):

* `OPENAI_API_KEY`: Sua chave de API da OpenAI.
* `OPENAI_ASSISTANT_ID`: O ID do seu assistente.
* `VECTOR_STORE_ID`: O ID do seu banco de dados vetorial.

## Estrutura do Projeto

```markdown
.env
.env-template
.gitignore
.streamlit/
    secrets.toml
app.py
data/
    guia_completo_sobre_regulamentacao_de_consorcios_no_brasil.txt
    L11795.pdf
    ResolucaoBCB285.pdf
entities/
    __init__.py
    agent.py
    openai_client.py
    threads.py
    vectordb.py
files/
    threads.txt
    urls.txt
requirements.txt
scripts/
    url_scrapper.py
```


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

Para qualquer dúvida, entre em contato com os mantenedores do projeto.
