import urllib.parse
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import io
import urllib, base64
from django.shortcuts import render

# Stock data time frame and abbreviation
ticker = ['AAPL', 'GOOGL', 'MSFT']

charts = []

for company_names in ticker:
    stock_data = yf.download(company_names, start='2019-01-01', end='2024-01-01')

    # Use only the closing price 
    df = stock_data[['Close']].copy()  # Use the 'Close' column only

    # Fill any missing values
    df['Close'] = df['Close'].fillna(method='ffill')

    # Create features (X) and target (y)
    # We'll use the past 5 days to predict the next day's closing price
    N = 5  # Gap between days it takes data (short term trends)
    X, y = [], []

    for i in range(N, len(df)):
        X.append(df['Close'].values[i-N:i])  # Features are the previous N days
        y.append(df['Close'].values[i])      # Predicts the next days closing price

    # Convert to numpy arrays
    X, y = np.array(X), np.array(y)

    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # prediction test
    y_pred = model.predict(X_test)

    # Model Percent error check
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')


    plt.figure(figsize=(12, 6))

    # Actual plot
    plt.plot(df.index[-len(y_test):], y_test, label='Actual Price', color='blue')

    # Predicted plot
    plt.plot(df.index[-len(y_test):], y_pred, label='Predicted Price', color='red')

    plt.title(f'({company_names}) Actual vs Predicted Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    string= base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    charts.append(uri)

