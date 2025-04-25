import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

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