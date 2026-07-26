import pandas as pd
import requests
import streamlit as st
URL_API = "https://smart-barreira.vercel.app/leituras"
def buscar_exames() -> pd.DataFrame:
    """Busca os exames na API e devolve como uma tabela do pandas."""
    resposta = requests.get(URL_API)
    return pd.DataFrame(resposta.json())

st.set_page_config(page_title="smartbarreira", page_icon="💧")

st.title("Painel da SmartBarreira")
tabela = buscar_exames()
if tabela.empty:
    st.info("Ainda nao chegaram exames da agua...")
else:
    ultimo = tabela.iloc[0]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("pH", f"{ultimo['ph']:.1f}")
    c2.metric("Turbidez", f"{ultimo['turbidez']}")
    c3.metric("TDS", f"{ultimo['tds']} ppm")
    c4.metric("Temperatura", f"{ultimo['temperatura']} C")
    
st.subheader("Historico do pH")
grafico = tabela.set_index("criado_em")["ph"]
st.line_chart(grafico)
