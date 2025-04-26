import streamlit as st
import pickle
import pandas as pd

# Carrega o modelo treinado
with open("modelo_random_forest_pix.pkl", "rb") as f:
    modelo = pickle.load(f)

# Base de dados simulada de chaves com histórico de fraude
chaves_suspeitas = [
    "99638194710",
    "55522120872",
    "86281025445"
]

# Título
st.markdown("## 🛡️ Sistema de Prevenção a Fraudes no PIX")

st.markdown("Preencha os dados da transação para verificar se será **Autorizada** ou **Não Autorizada**:")

# Coleta de dados
valor = st.number_input("Valor da transação (R$)", min_value=0.0, step=10.0)
hora = st.slider("Hora da transação", min_value=0, max_value=23)
localizacao = st.selectbox("Localização", ["SP", "RJ", "MG", "BA", "RS"])
tipo_conta = st.selectbox("Tipo de conta", ["corrente", "poupanca", "salario"])
chave_pix = st.text_input("Chave PIX de destino (telefone, CPF, email...)")

# Mapeia as entradas
dados = {
    "valor": valor,
    "hora": hora,
    "localizacao": {"SP": 0, "RJ": 1, "MG": 2, "BA": 3, "RS": 4}[localizacao],
    "tipo_conta": {"corrente": 0, "poupanca": 1, "salario": 2}[tipo_conta],
    "chave_historico_fraude": True if chave_pix in chaves_suspeitas else False
}

df = pd.DataFrame([dados])

# Botão para simular a transação
if st.button("Verificar Transação"):
    pred = modelo.predict(df)[0]
    if pred == 1:
        st.error("🚫 Transação NÃO AUTORIZADA (Suspeita de Fraude)")
    else:
        st.success("✅ Transação AUTORIZADA")

