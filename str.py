import yfinance as yf
import pandas as pd

# Function to fetch live stock data
def fetch_live_data(symbol):
    data = yf.download(symbol, period="1d", interval="1m")
    return data

# Function to calculate moving averages
def calculate_moving_averages(data, short_window, long_window):
    data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window).mean()
    return data

# Function to generate buy/sell signals based on moving average crossover
def generate_signals(data):
    signals = []
    position = 0
    
    for i in range(1, len(data)):
        if data['Short_MA'].iloc[i] > data['Long_MA'].iloc[i] and data['Short_MA'].iloc[i - 1] <= data['Long_MA'].iloc[i - 1]:
            signals.append(1)  # Buy signal
            position = 1
        elif data['Short_MA'].iloc[i] < data['Long_MA'].iloc[i] and data['Short_MA'].iloc[i - 1] >= data['Long_MA'].iloc[i - 1]:
            signals.append(-1)  # Sell signal
            position = 0
        else:
            signals.append(0)  # No signal
    
    return signals

# Main function for live trading
def live_trading(symbol):
    # Fetch live data
    live_data = fetch_live_data(symbol)
    
    # Calculate moving averages
    live_data = calculate_moving_averages(live_data, 50, 200)
    
    # Generate buy/sell signals
    signals = generate_signals(live_data)
    
    # Print signals
    print(signals)  # Replace this with actual trading logic

# Example usage
if __name__ == "__main__":
    symbol = 'AAPL'  # Example stock symbol
    live_trading(symbol)
