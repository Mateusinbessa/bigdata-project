import pandas as pd
import streamlit as st

data = pd.read_csv('barbearia_dados.csv')

st.title("Dashboard de Barbearia")

st.subheader("Dados Brutos")
st.dataframe(data)

st.sidebar.header("Filtros")

barbeiro = st.sidebar.multiselect(
    "Escolha o(s) Barbeiro(s):",
    options=data["Barbeiro"].unique(),
    default=data["Barbeiro"].unique()
)

servico = st.sidebar.multiselect(
    "Escolha o(s) Serviço(s):",
    options=data["Serviço"].unique(),
    default=data["Serviço"].unique()
)

pagamento = st.sidebar.multiselect(
    "Forma de Pagamento:",
    options=data["Forma de Pagamento"].unique(),
    default=data["Forma de Pagamento"].unique()
)

filtered_data = data[
    (data["Barbeiro"].isin(barbeiro)) &
    (data["Serviço"].isin(servico)) &
    (data["Forma de Pagamento"].isin(pagamento))
]

st.subheader("Dados Filtrados")
st.dataframe(filtered_data)

st.subheader("Métricas Gerais")

receita_total = filtered_data["Valor (R$)"].sum()
st.metric("Receita Total (R$)", f"{receita_total:.2f}")

total_atendimentos = len(filtered_data)
st.metric("Total de Atendimentos", total_atendimentos)

st.subheader("Visualizações")

receita_por_servico = filtered_data.groupby("Serviço")["Valor (R$)"].sum()
st.bar_chart(receita_por_servico)

receita_por_barbeiro = filtered_data.groupby("Barbeiro")["Valor (R$)"].sum()
st.bar_chart(receita_por_barbeiro)

receita_por_pagamento = filtered_data.groupby("Forma de Pagamento")["Valor (R$)"].sum()
st.bar_chart(receita_por_pagamento)

# Rodar com streamlit
# streamlit run main.py
