import yfinance as yf
import pandas as pd
import streamlit as st

st.title("Stock Analysis Dashboard")

ticker = st.text_input("Enter Stock Ticker (e.g. AAPL)", "AAPL")

data = yf.download(ticker, start="2020-01-01")

st.subheader("Raw Data")
st.write(data.tail())

data['Returns'] = data['Close'].pct_change()

st.subheader("Returns")
st.line_chart(data['Returns'])

data['MA50'] = data['Close'].rolling(50).mean()
data['MA200'] = data['Close'].rolling(200).mean()

st.subheader("Moving Averages")
st.line_chart(data[['Close', 'MA50', 'MA200']])

volatility = data['Returns'].std() * (252 ** 0.5)
st.write(f"Annualized Volatility: {volatility:.2f}")
