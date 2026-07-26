import pandas as pd
import requests
import streamlit as st
URL_API = "https://smart-barreira.vercel.app/leituras"
def buscar_exames() -> pd.DataFrame:
    """Busca os exames na API e devolve como uma tabela do pandas."""
    resposta = requests.get(URL_API)
    return pd.DataFrame(resposta.json())

st.set_page_config(page_title="SmartBarreira", page_icon="💧")

st.title("Painel da SmartBarreira")
st.markdown('<meta http-equiv="refresh" content="30">', unsafe_allow_html=True)

tabela = buscar_exames()

if tabela.empty:
    st.info("Ainda nao chegaram exames da agua...")
else:
    ultimo = tabela.iloc[0]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("pH", f"{ultimo['ph']:.1f}")
    c2.metric("Turbidez", f"{ultimo['turbidez']}")
    c3.metric("Qualidade da Agua", f"{ultimo['tds']} ppm")
    c4.metric("Temperatura", f"{ultimo['temperatura']} C")
    
st.subheader("Historico do pH")
grafico = tabela.set_index("criado_em")[["ph", "turbidez", "tds", "temperatura"]]
st.line_chart(grafico)
