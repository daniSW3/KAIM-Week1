import pandas as pd
import talib
import pynance as pn
import matplotlib.pyplot as plt


def load_stock_data(file_path):
    """Load stock price data into a pandas DataFrame."""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df


def calculate_technical_indicators(df):
    """Calculate technical indicators using TA-Lib."""
    # Simple Moving Average (SMA)
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    # Relative Strength Index (RSI)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    # Moving Average Convergence Divergence (MACD)
    df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = talib.MACD(
        df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return df


def calculate_financial_metrics(df):
    """Calculate financial metrics using PyNance."""
    returns = pn.data.returns(df['Close'])
    volatility = pn.stats.volatility(df['Close'])
    print(f"Annualized Volatility: {volatility:.4f}")
    return returns


def visualize_data(df):
    """Visualize stock price and technical indicators."""
    plt.figure(figsize=(12, 8))

    # Plot Close Price and SMA
    plt.subplot(3, 1, 1)
    plt.plot(df.index, df['Close'], label='Close Price')
    plt.plot(df.index, df['SMA_20'], label='20-day SMA')
    plt.title('Stock Price and SMA')
    plt.legend()

    # Plot RSI
    plt.subplot(3, 1, 2)
    plt.plot(df.index, df['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title('Relative Strength Index (RSI)')
    plt.legend()

    # Plot MACD
    plt.subplot(3, 1, 3)
    plt.plot(df.index, df['MACD'], label='MACD', color='blue')
    plt.plot(df.index, df['MACD_Signal'], label='Signal Line', color='orange')
    plt.bar(df.index, df['MACD_Hist'],
            label='MACD Histogram', color='grey', alpha=0.3)
    plt.title('MACD')
    plt.legend()

    plt.tight_layout()
    plt.savefig('technical_indicators.png')
    plt.close()


if __name__ == "__main__":
    # Example usage
    df = load_stock_data('stock_data.csv')  # Replace with actual data path
    df = calculate_technical_indicators(df)
    returns = calculate_financial_metrics(df)
    visualize_data(df)
