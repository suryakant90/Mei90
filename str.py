import streamlit as st
import yfinance as yf

# Set up the Streamlit app
st.title('Stock Technical Analysis')

# Input field for stock symbol
stock_symbol = st.text_input('Enter Stock Symbol (e.g., AAPL):')

# Fetch real-time data from Yahoo Finance
@st.cache
def get_stock_data(symbol):
    return yf.download(symbol, start="2023-01-01", end="2024-01-01")

if stock_symbol:
    stock_data = get_stock_data(stock_symbol)

    # Display the TradingView chart using the HTML component
    chart_html = """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div id="tradingview_123456"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
      {
      "autosize": true,
      "symbol": "NASDAQ:AAPL",
      "interval": "D",
      "timezone": "Etc/UTC",
      "theme": "light",
      "style": "1",
      "locale": "en",
      "toolbar_bg": "#f1f3f6",
      "enable_publishing": false,
      "withdateranges": true,
      "hide_side_toolbar": false,
      "allow_symbol_change": true,
      "details": true,
      "hotlist": true,
      "calendar": true,
      "studies": [
        "BB@tv-basicstudies",
        "MACD@tv-basicstudies"
      ],
      "show_popup_button": true,
      "popup_width": "1000",
      "popup_height": "650",
      "container_id": "tradingview_123456"
    }
      );
      </script>
    </div>
    <!-- TradingView Widget END -->
    """
    st.components.v1.html(chart_html, width=1000, height=650)

    # Calculate 200-day low and high
    low_200 = stock_data['Low'].rolling(window=200).min().dropna()
    high_200 = stock_data['High'].rolling(window=200).max().dropna()

    # Display the 200-day low and high
    st.subheader('200-Day Low and High')
    st.write(f"Low: {low_200.iloc[-1]}")
    st.write(f"High: {high_200.iloc[-1]}")
