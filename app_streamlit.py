import streamlit as st
import pickle
import pandas as pd
import requests

# Baixa o modelo do GitHub (binário)
url_modelo = "https://raw.githubusercontent.com/SilvinhaPatty/modelo-antifraude-pix/main/modelo_random_forest_pix.pkl"
resposta = requests.get(url_modelo)
with open("modelo_random_forest_pix.pkl", "wb") as f:
    f.write(resposta.content)

# Carrega o modelo
with open("modelo_random_forest_pix.pkl", "rb") as f:
    modelo = pickle.load(f)

# Título do aplicativo
st.title("🔍 Verificador de Fraudes no PIX")

st.markdown("Preencha os dados da transação abaixo para verificar se há suspeita de fraude:")

# Coleta de dados simulados do usuário
valor = st.number_input("Valor da transação (R$)", min_value=0.0, step=10.0)
hora = st.slider("Hora da transação", min_value=0, max_value=23)
localizacao = st.selectbox("Localização", ["SP", "RJ", "MG", "BA", "RS"])
tipo_conta = st.selectbox("Tipo de conta", ["corrente", "poupanca", "salario"])
chave_historico_fraude = st.selectbox("Esta chave já esteve envolvida em fraude?", ["Sim", "Não"])

# Mapeia os dados como no modelo
dados = {
    "valor": valor,
    "hora": hora,
    "localizacao": {"SP": 0, "RJ": 1, "MG": 2, "BA": 3, "RS": 4}[localizacao],
    "tipo_conta": {"corrente": 0, "poupanca": 1, "salario": 2}[tipo_conta],
    "chave_historico_fraude": True if chave_historico_fraude == "Sim" else False
}

df = pd.DataFrame([dados])

# Botão para prever
if modelo is None:
    st.error("❌ O modelo não foi carregado corretamente. Verifique o download.")
else:
    pred = modelo.predict(df)[0]
    if pred == 1:
        st.error("🚨 Suspeita de FRAUDE detectada na transação!")
    else:
        st.success("✅ Transação considerada legítima.")

