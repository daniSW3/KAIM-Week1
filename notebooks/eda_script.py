from visualization.plot_utils import plot_publication_trend, plot_publisher_domains
from analysis.publisher_analysis import analyze_publishers
from analysis.text_analysis import extract_topics
from analysis.descriptive_stats import compute_descriptive_stats
from data.news_loader import load_news_data
import sys
import os

# Add src/ to Python path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'src')))


def main():
    print("Exploratory Data Analysis (EDA) for Stock News Data")
    print("--------------------------------------------------")

    # Load the data
    news_file = '../news_data.csv'  # Replace with actual path
    print("Loading data...")
    df = load_news_data(news_file)
    print("Data preview:")
    print(df.head())

    # Descriptive Statistics
    print("\nDescriptive Statistics")
    print("----------------------")
    stats = compute_descriptive_stats(df)
    print("Headline Length Statistics:")
    print(stats['headline_stats'])
    print("\nTop Publishers:")
    print(stats['publisher_counts'].head(10))
    print("\nPlotting publication trend...")
    plot_publication_trend(stats['daily_counts'])

    # Text Analysis
    print("\nText Analysis")
    print("-------------")
    df = extract_topics(df, max_features=1000)
    print("Top Terms per Headline (Sample):")
    print(df[['headline', 'top_terms']].head())

    # Publisher Analysis
    print("\nPublisher Analysis")
    print("-----------------")
    domain_counts = analyze_publishers(df)
    print("Top Publisher Domains:")
    print(domain_counts.head(10))
    print("\nPlotting publisher domains...")
    plot_publisher_domains(domain_counts)

    # Additional Exploration
    print("\nAdditional Exploration")
    print("---------------------")
    # Example: Filter data by a specific publisher
    specific_publisher = 'example.com'  # Replace with actual domain
    filtered_df = df[df['domain'] == specific_publisher]
    print(f"Data for publisher domain '{specific_publisher}':")
    print(filtered_df.head())


if __name__ == "__main__":
    main()
