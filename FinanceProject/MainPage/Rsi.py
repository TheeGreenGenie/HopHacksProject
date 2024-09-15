import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

# Define a function to calculate the RSI
def calculate_rsi(data, window=14):
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Fetch stock data
tickers = ['NVDA', 'AAPL']
stock_data = {}
for ticker in tickers:
    stock_data[ticker] = yf.download(ticker, period='1y')

# Calculate RSI for both stocks
for ticker in stock_data:
    stock_data[ticker]['RSI'] = calculate_rsi(stock_data[ticker])

# Plot the RSI for both Nvidia and Apple
plt.figure(figsize=(10, 6))

plt.plot(stock_data['NVDA'].index, stock_data['NVDA']['RSI'], label='NVDA RSI', color='blue', linewidth=2)
plt.plot(stock_data['AAPL'].index, stock_data['AAPL']['RSI'], label='AAPL RSI', color='green', linewidth=2)

plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
plt.axhline(30, color='red', linestyle='--', label='Oversold (30)')

plt.title('RSI Comparison of Nvidia (NVDA) and Apple (AAPL)', fontsize=16)
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend(loc='best')
plt.grid(True)


buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()
graphic = base64.b64encode(image_png)
graph3 = graphic.decode('utf-8')
