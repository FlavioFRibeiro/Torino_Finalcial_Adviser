# File: /Torino_Financial_Advisor/Torino_Financial_Advisor/web_app/app.py

import streamlit as st
from analytics.data_extraction import data_extraction
from analytics.plot_utils import plot_stock_price, plot_candlestick, plot_media_movel, plot_volume
from ai_agents.agents import multi_ai_agent
import re

def run_app():
    # Configuração da página do Streamlit
    st.set_page_config(page_title="Torino AI", page_icon="💰🦬", layout="wide")

    # Barra Lateral com instruções
    from .sidebar import display_sidebar
    display_sidebar()

    # Título principal
    st.title("💰🦬 Torino - O AI Financial Advisor")

    # Interface principal
    st.header("Stocks Analytics em Tempo Real com o Torino 🦬")

    # Caixa de texto para input do usuário
    ticker = st.text_input("Digite o Código da Ação Desejada:").upper()

    # Se o usuário pressionar o botão, entramos neste bloco
    if st.button("Analisar"):

        # Se temos o código da ação (ticker)
        if ticker:

            # Inicia o processamento
            with st.spinner("Buscando os Dados em Tempo Real. Aguarde..."):
                
                # Obtém os dados
                hist = data_extraction(ticker)
                
                # Renderiza um subtítulo
                st.subheader("Análise Gerada pelo Torino 🦬")
                
                # Executa o time de Agentes de IA
                ai_response = multi_ai_agent.run(f"Resumir a recomendação do analista e compartilhar as últimas notícias para {ticker}")

                # Remove linhas que começam com "Running:"
                clean_response = re.sub(r"(Running:[\s\S]*?\n\n)|(^transfer_task_to_finance_ai_agent.*\n?)","", ai_response.content, flags=re.MULTILINE).strip()

                # Imprime a resposta
                st.markdown(clean_response)

                # Renderiza os gráficos
                st.subheader("Visualização dos Dados")
                plot_stock_price(hist, ticker)
                plot_candlestick(hist, ticker)
                plot_media_movel(hist, ticker)
                plot_volume(hist, ticker)
        else:
            st.error("Ticker inválido. Insira um símbolo de ação válido para o Torino trabalhar.")