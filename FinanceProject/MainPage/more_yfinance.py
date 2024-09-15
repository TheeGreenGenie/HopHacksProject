import yfinance as yf
import pandas as pd

# List of stock tickers to analyze
tickers = ['AAPL', 'MSFT', 'TSLA', 'GOOGL', 'AMZN', 'NVDA', 'FB']

# Function to get percentage change in stock price over a given period
def get_stock_performance(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)

    # Calculate percentage change
    start_price = hist['Close'][0]
    end_price = hist['Close'][-1]
    percent_change = ((end_price - start_price) / start_price) * 100

    return percent_change

# Create an empty list to store stock performance data
performance_data = []

# Get performance for each stock in the list
for ticker in tickers:
    try:
        performance = get_stock_performance(ticker, period='1mo')
        performance_data.append({'Ticker': ticker, 'Performance (%)': performance})
    except Exception as e:
        print(f"Could not retrieve data for {ticker}: {e}")

# Convert the list to a DataFrame for better analysis
df = pd.DataFrame(performance_data)

# Sort by performance to find the highest-performing stocks
df = df.sort_values(by='Performance (%)', ascending=False)