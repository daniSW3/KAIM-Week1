import matplotlib.pyplot as plt
import seaborn as sns

def plot_publication_trend(daily_counts):
    """Plot article publication frequency over time."""
    plt.figure(figsize=(10, 6))
    daily_counts.plot()
    plt.title('Article Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.savefig('publication_trend.png')
    plt.show()
    plt.close()

def plot_publisher_domains(domain_counts):
    """Plot top publisher domains."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x=domain_counts.head(10).values, y=domain_counts.head(10).index)
    plt.title('Top 10 Publisher Domains')
    plt.xlabel('Number of Articles')
    plt.savefig('publisher_domains.png')
    plt.show()
    plt.close()

def plot_technical_indicators(df):
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
    plt.bar(df.index, df['MACD_Hist'], label='MACD Histogram', color='grey', alpha=0.3)
    plt.title('MACD')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('technical_indicators.png')
    plt.show()
    plt.close()