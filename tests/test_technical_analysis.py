import unittest
import pandas as pd
from src.data.stock_loader import load_stock_data
from src.analysis.technical_analysis import calculate_technical_indicators

class TestTechnicalAnalysis(unittest.TestCase):
    def test_technical_indicators(self):
        # Mock data
        data = pd.DataFrame({
            'Date': ['2023-01-01', '2023-01-02', '2023-01-03'] * 10,
            'Close': [100, 101, 102] * 10,
            'Open': [99, 100, 101] * 10,
            'High': [101, 102, 103] * 10,
            'Low': [98, 99, 100] * 10,
            'Volume': [1000, 1100, 1200] * 10
        })
        data.to_csv('test_stock.csv', index=False)
        
        df = load_stock_data('test_stock.csv')
        df = calculate_technical_indicators(df)
        self.assertIn('SMA_20', df.columns)
        self.assertIn('RSI', df.columns)
        self.assertIn('MACD', df.columns)
        
if __name__ == '__main__':
    unittest.main()