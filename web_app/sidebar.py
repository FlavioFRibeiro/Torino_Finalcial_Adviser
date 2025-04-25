# sidebar.py

import streamlit as st

def display_sidebar():
    st.sidebar.title("Instruções")
    st.sidebar.markdown("""
    ### Como Utilizar a App:

    - Insira o símbolo do ticker da ação desejada no campo central.
    - Clique no botão **Analisar** para obter a análise em tempo real com visualizações e insights gerados pelo Torino.

    ### Exemplos de tickers válidos:
    - MSFT (Microsoft)
    - TSLA (Tesla)
    - AMZN (Amazon)
    - GOOG (Alphabet)

    Mais tickers podem ser encontrados aqui: https://stockanalysis.com/list/nasdaq-stocks/

    ### Finalidade da App:
    Este aplicativo realiza análises avançadas de preços de ações da Nasdaq em tempo real utilizando Agentes de IA com modelo DeepSeek através do Groq para apoio a investidores (profissionais ou não).
    """)

    # Botão de suporte na barra lateral
    if st.sidebar.button("Suporte"):
        st.sidebar.write("No caso de dúvidas ou problemas envie e-mail para: flarib@msn.com")