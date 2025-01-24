# Projeto de Pesquisa em CSV com Flask e Vue.js

Este é um projeto que combina uma API Flask para manipulação de dados em um arquivo CSV e uma interface de usuário feita com Vue.js para buscar informações nesse arquivo.

## Descrição

A aplicação permite que o usuário insira um termo para pesquisar no arquivo CSV. A API, construída com Flask, retorna as linhas que contêm o termo pesquisado na coluna "Razao_Social". O front-end em Vue.js oferece uma interface limpa e responsiva para interação com o usuário.

## Tecnologias Utilizadas

- **Back-end:** Flask (Python)
- **Front-end:** Vue.js (JavaScript)
- **Banco de Dados:** Arquivo CSV

## Requisitos

- Python 3.x
- Flask
- Flask-CORS
- Vue.js
- Node.js e npm (para o front-end)

## Instalação

### 1. Instalação do Back-End

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/macOS
    venv\Scripts\activate     # Para Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Coloque o arquivo CSV chamado `Relatorio_cadop.csv` na raiz do projeto ou ajuste o caminho no código.

5. Execute a aplicação Flask:

    ```bash
    python app.py
    ```

   O servidor Flask estará rodando em `http://127.0.0.1:5000`.

### 2. Instalação do Front-End

1. Navegue até o diretório do front-end e instale as dependências:

    ```bash
    cd frontend
    npm install
    ```

2. Execute a aplicação Vue.js:

    ```bash
    npm run serve
    ```

   A interface será acessível em `http://localhost:8080`.

## Uso

1. Abra a interface Vue.js no navegador (`http://localhost:8080`).
2. Digite um termo na caixa de pesquisa e pressione Enter ou clique no botão "Pesquisar".
3. A lista de resultados será exibida abaixo da caixa de pesquisa, mostrando as entradas do arquivo CSV que contêm o termo pesquisado na coluna "Razao_Social".

## Estrutura de Arquivos

