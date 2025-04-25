import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Carrega o modelo Random Forest treinado (salvo com pickle)
with open("modelo_random_forest_pix.pkl", "rb") as f:
    modelo = pickle.load(f)

# Cria a aplicação Flask
app = Flask(__name__)

# Rota inicial para verificar se a API está no ar
@app.route('/')
def home():
    return '🚀 API Antifraude PIX está no ar!'

# Rota para prever fraude com base nos dados recebidos via POST
@app.route('/prever', methods=['POST'])
def prever():
    try:
        # Coleta os dados JSON enviados na requisição
        dados = request.json

        # Converte o dicionário recebido em DataFrame para o modelo
        df = pd.DataFrame([dados])

        # Codifica colunas categóricas como foi feito no treinamento
        df['tipo_conta'] = df['tipo_conta'].map({'corrente': 0, 'poupanca': 1, 'salario': 2}).fillna(0)
        df['localizacao'] = df['localizacao'].map({'SP': 0, 'RJ': 1, 'MG': 2, 'BA': 3, 'RS': 4}).fillna(0)

        # Faz a previsão com o modelo carregado
        predicao = modelo.predict(df)[0]

        # Retorna o resultado como JSON
        return jsonify({'fraude': bool(predicao)})

    except Exception as e:
        # Em caso de erro, retorna uma mensagem amigável
        return jsonify({'erro': 'Erro ao processar a previsão', 'detalhes': str(e)}), 400

# Executa a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
