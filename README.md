# 🔍 Projeto: Verificador de Fraudes no PIX

Este projeto tem como objetivo construir um modelo de Machine Learning para identificar transações suspeitas de fraude via PIX. A solução combina a geração de dados sintéticos, aplicação de regras de negócio e treinamento de modelo supervisionado com Random Forest.

---

## 📁 Estrutura do Projeto

```
Projeto_Antifraude_PIX
│
├── app_streamlit.py                # Interface com Streamlit
├── dados_pix_sinteticos.csv        # Base de dados gerada
├── main.py                         # Código auxiliar (opcional)
├── modelo_pix_antifraude.ipynb     # Notebook com geração de dados e modelo
├── modelo_random_forest_pix.pkl    # Modelo Random Forest treinado
├── replit.txt                      # Arquivo auxiliar do ambiente (opcional)
└── requirements.txt                # Dependências do projeto
```

---

## 🧠 Lógica da Detecção de Fraude

A transação será classificada como **fraude** se atender a uma ou mais das seguintes condições:

- A chave já teve fraude (`chave_historico_fraude = True`)
- Valor da transação > 2000
- Transação entre 0h e 6h
- Valor > 1000 **e** transação entre 0h e 6h

---

## 🧪 Como executar localmente

1. Clone este repositório
2. Crie um ambiente virtual (recomendado)
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o aplicativo Streamlit:

```bash
streamlit run app_streamlit.py
```

---

## 📦 Tecnologias e Bibliotecas

- Python 3.13
- Pandas
- Scikit-learn
- Streamlit
- Random Forest (sklearn.ensemble)

---

## 👩‍💻 Autoria

Silvia Patricia · Projeto integrador de pós-graduação em Data Science · Unoeste · 2025
