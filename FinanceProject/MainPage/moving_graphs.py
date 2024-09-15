import yfinance as yf
import pandas as pd
import base64
import io

# Define the stock tickers
tickers = ['NVDA', 'AAPL']

# Fetch data for both tickers
stock_data = {}
for ticker in tickers:
    stock_data[ticker] = yf.download(ticker, period='1y')  # Getting one year of data

# Calculate the moving averages (20-day, 50-day, and 200-day)
for ticker in stock_data:
    stock_data[ticker]['MA_20'] = stock_data[ticker]['Close'].rolling(window=20).mean()
    stock_data[ticker]['MA_50'] = stock_data[ticker]['Close'].rolling(window=50).mean()
    stock_data[ticker]['MA_200'] = stock_data[ticker]['Close'].rolling(window=200).mean()

# Display the data for both tickers
print(stock_data['NVDA'].tail())  # Display the last few entries for Nvidia
print(stock_data['AAPL'].tail())  # Display the last few entries for Apple

import matplotlib.pyplot as plt

# Combined plot for both NVDA and AAPL stock data with moving averages
plt.figure(figsize=(12,8))

# Plot for Nvidia
plt.plot(stock_data['NVDA'].index, stock_data['NVDA']['Close'], label='NVDA Closing Price', color='blue', linewidth=2)
plt.plot(stock_data['NVDA'].index, stock_data['NVDA']['MA_20'], label='NVDA 20-Day MA', linestyle='--', color='lightblue')
plt.plot(stock_data['NVDA'].index, stock_data['NVDA']['MA_50'], label='NVDA 50-Day MA', linestyle='--', color='cyan')
plt.plot(stock_data['NVDA'].index, stock_data['NVDA']['MA_200'], label='NVDA 200-Day MA', linestyle='--', color='darkblue')

# Plot for Apple
plt.plot(stock_data['AAPL'].index, stock_data['AAPL']['Close'], label='AAPL Closing Price', color='green', linewidth=2)
plt.plot(stock_data['AAPL'].index, stock_data['AAPL']['MA_20'], label='AAPL 20-Day MA', linestyle='--', color='lightgreen')
plt.plot(stock_data['AAPL'].index, stock_data['AAPL']['MA_50'], label='AAPL 50-Day MA', linestyle='--', color='lime')
plt.plot(stock_data['AAPL'].index, stock_data['AAPL']['MA_200'], label='AAPL 200-Day MA', linestyle='--', color='darkgreen')

# Titles and labels
plt.title('NVIDIA (NVDA) and Apple (AAPL) Stock Prices with Moving Averages', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend(loc='best')
plt.grid(True)

buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()
graphic = base64.b64encode(image_png)
graph1 = graphic.decode('utf-8')
