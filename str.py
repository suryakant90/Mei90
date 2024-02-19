import pandas as pd
import numpy as np
import talib

# Load historical data (you can fetch this data from various sources like Yahoo Finance or NSE/BSE APIs)
# For simplicity, let's assume you have a CSV file containing OHLCV (Open, High, Low, Close, Volume) data
data = pd.read_csv('historical_data.csv')

# Convert the date column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the date column as the index
data.set_index('Date', inplace=True)

# Resample the data to 5-minute intervals (adjust as per your requirement)
data_5min = data.resample('5T').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})

# Calculate technical indicators (you can use various indicators based on your strategy)
data_5min['SMA_50'] = talib.SMA(data_5min['Close'], timeperiod=50)
data_5min['SMA_200'] = talib.SMA(data_5min['Close'], timeperiod=200)
data_5min['RSI'] = talib.RSI(data_5min['Close'], timeperiod=14)

# Define your trading strategy
data_5min['Signal'] = np.where((data_5min['SMA_50'] > data_5min['SMA_200']) & (data_5min['RSI'] < 30), 1, 0)

# Backtest the strategy
data_5min['Returns'] = data_5min['Close'].pct_change()
data_5min['Strategy_Returns'] = data_5min['Signal'].shift(1) * data_5min['Returns']

# Calculate cumulative returns
data_5min['Cumulative_Returns'] = (1 + data_5min['Strategy_Returns']).cumprod()

# Plot cumulative returns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(data_5min['Cumulative_Returns'], label='Strategy Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.title('Intraday Trading Strategy Returns')
plt.legend()
plt.grid(True)
plt.show()
