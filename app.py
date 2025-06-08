# Imports
import re
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

# Carrega o arquivo de variáveis de ambiente
load_dotenv()

def data_extraction(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    hist.reset_index(inplace=True)
    return hist

def plot_stock_price(hist, ticker):
    fig = px.line(hist, x="Date", y="Close", title=f"{ticker} Preços das Ações (Últimos 6 Meses)", markers=True)
    st.plotly_chart(fig)

def plot_candlestick(hist, ticker):
    fig = go.Figure(data=[go.Candlestick(x=hist['Date'],
                                          open=hist['Open'],
                                          high=hist['High'],
                                          low=hist['Low'],
                                          close=hist['Close'])])
    fig.update_layout(title=f"{ticker} Candlestick Chart (Últimos 6 Meses)")
    st.plotly_chart(fig)

def plot_media_movel(hist, ticker):
    hist['SMA_20'] = hist['Close'].rolling(window=20).mean()
    hist['EMA_20'] = hist['Close'].ewm(span=20, adjust=False).mean()
    fig = px.line(hist, 
                  x='Date', 
                  y=['Close', 'SMA_20', 'EMA_20'],
                  title=f"{ticker} Médias Móveis (Últimos 6 Meses)",
                  labels={'value': 'Price (USD)', 'Date': 'Date'})
    st.plotly_chart(fig)

def plot_volume(hist, ticker):
    fig = px.bar(hist, 
                 x='Date', 
                 y='Volume', 
                 title=f"{ticker} Trading Volume (Últimos 6 Meses)")
    st.plotly_chart(fig)

agente_web_search = Agent(
    name="Torino Agente Web Search",
    role="Fazer busca na web",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGo()],
    instructions=["Sempre inclua as fontes"],
    show_tool_calls=True,
    markdown=True
)

agente_financeiro = Agent(
    name="Torino Agente Financeiro",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["Sempre use tabelas para mostrar os dados"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team=[agente_web_search, agente_financeiro],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=["Sempre inclua as fontes",
                  "Sempre use tabelas para mostrar os dados"],
    show_tool_calls=True,
    markdown=True
)


# Configuração do Streamlit

# Configuração da página do Streamlit
st.set_page_config(page_title="Torino AI", page_icon="💰🦬", layout="wide")

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



# Título principal
st.title("💰🦬 Torino - O AI Financial Advisor")

# Interface principal
st.header("Stocks Analytics em Tempo Real")

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