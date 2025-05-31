from data.news_loader import load_news_data
from data.stock_loader import load_stock_data
from analysis.descriptive_stats import compute_descriptive_stats
from analysis.text_analysis import extract_topics
from analysis.publisher_analysis import analyze_publishers
from analysis.technical_analysis import calculate_technical_indicators, calculate_financial_metrics
from visualization.plot_utils import plot_publication_trend, plot_publisher_domains, plot_technical_indicators


def run_eda(file_path):
    """Run Exploratory Data Analysis."""
    df = load_news_data(file_path)
    stats = compute_descriptive_stats(df)
    print("Headline Length Statistics:")
    print(stats['headline_stats'])
    print("\nTop Publishers:")
    print(stats['publisher_counts'].head(10))
    plot_publication_trend(stats['daily_counts'])

    df = extract_topics(df)
    print("\nTop Terms per Headline (Sample):")
    print(df[['headline', 'top_terms']].head())

    domain_counts = analyze_publishers(df)
    print("\nTop Publisher Domains:")
    print(domain_counts.head(10))
    plot_publisher_domains(domain_counts)


def run_technical_analysis(file_path):
    """Run technical analysis."""
    df = load_stock_data(file_path)
    df = calculate_technical_indicators(df)
    returns, volatility = calculate_financial_metrics(df)
    print(f"Annualized Volatility: {volatility:.4f}")
    plot_technical_indicators(df)


if __name__ == "__main__":
    # Replace with actual data paths
    news_file = 'news_data.csv'
    stock_file = 'stock_data.csv'
    run_eda(news_file)
    run_technical_analysis(stock_file)
