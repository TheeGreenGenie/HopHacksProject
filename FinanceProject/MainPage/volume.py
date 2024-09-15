import yfinance as yf
import matplotlib.pyplot as plt
import base64
import io

# Fetch stock data
tickers = ['NVDA', 'AAPL']
stock_data = {}
for ticker in tickers:
    stock_data[ticker] = yf.download(ticker, period='1y')

# Plot the trading volume for both Nvidia and Apple
plt.figure(figsize=(10, 6))

# Plot NVDA's volume
plt.plot(stock_data['NVDA'].index, stock_data['NVDA']['Volume'], label='NVDA Volume', color='blue', linewidth=2)

# Plot AAPL's volume
plt.plot(stock_data['AAPL'].index, stock_data['AAPL']['Volume'], label='AAPL Volume', color='green', linewidth=2)

# Titles and labels
plt.title('Volume Comparison of Nvidia (NVDA) and Apple (AAPL)', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend(loc='best')
plt.grid(True)


buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()
graphic = base64.b64encode(image_png)
graph2 = graphic.decode('utf-8')

