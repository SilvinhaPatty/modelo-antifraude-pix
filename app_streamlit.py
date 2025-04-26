import streamlit as st
import pickle
import pandas as pd

# 1) Carrega o modelo treinado
with open("modelo_random_forest_pix.pkl", "rb") as f:
    modelo = pickle.load(f)

# 2) Carrega a base sintética e extrai as chaves marcadas (forçando string)
df = pd.read_csv("dados_pix_sinteticos.csv", dtype={"chave_pix": str})
chaves_suspeitas = (
    df
    .loc[df["chave_historico_fraude"] == True, "chave_pix"]
    .unique()
    .tolist()
)

# 3) Define listas fixas para o formulário (evita depender do CSV)
ufs   = ["SP", "RJ", "MG", "PR", "RS", "BA"]
tipos = ["corrente", "poupanca", "salario"]

# 4) Layout da página
st.set_page_config(page_title="Prevenção a Fraudes no PIX", layout="centered")
st.title("🔒 Sistema de Prevenção a Fraudes no PIX")
st.markdown("Preencha os dados da transação para verificar se será **Autorizada** ou **Não Autorizada**:")

# 5) Campos de entrada
valor = st.number_input("Valor da transação (R$)", min_value=0.0, step=10.0, format="%.2f")
hora  = st.slider("Hora da transação", 0, 23, help="Horário do dia em que o PIX será executado")
local = st.selectbox("Localização", ufs)
tipo  = st.selectbox("Tipo de conta", tipos)
chave = st.text_input("Chave PIX de destino", placeholder="telefone, CPF, e-mail ou aleatória")

# 6) Mapeamentos para código do modelo
map_loc  = {uf: i for i, uf in enumerate(ufs)}
map_tipo = {tp: i for i, tp in enumerate(tipos)}

dados = {
    "valor": valor,
    "hora": hora,
    "localizacao": map_loc.get(local, 0),
    "tipo_conta": map_tipo.get(tipo, 0),
    "chave_historico_fraude": (chave in chaves_suspeitas)
}
X = pd.DataFrame([dados])

# 7) Botão de acionamento
if st.button("Verificar Transação"):
    pred = modelo.predict(X)[0]
    if pred == 1:
        st.error("🚫 Transação NÃO AUTORIZADA")
    else:
        st.success("✅ Transação AUTORIZADA")
