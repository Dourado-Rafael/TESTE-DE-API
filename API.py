from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Função para ler o CSV com o Pandas
def ler_csv():
    # Lê o arquivo CSV em um DataFrame
    return pd.read_csv('Relatorio_cadop.csv',delimiter=";")

# Rota para fazer a pesquisa
@app.route('/pesquisar', methods=['GET'])
def pesquisar():
    # Pega o parâmetro de pesquisa da URL
    termo = request.args.get('termo')

    # Lê os dados do CSV usando Pandas
    df = ler_csv()

    resultados = df[df["Razao_Social"].str.contains(termo,case=False)]

    resultados = resultados.where(pd.notnull(resultados), None)

    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
