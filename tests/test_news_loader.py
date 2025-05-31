import unittest
import pandas as pd
from src.data.news_loader import load_news_data

class TestNewsLoader(unittest.TestCase):
    def test_load_news_data(self):
        # Mock data
        data = pd.DataFrame({
            'headline': ['Test headline'],
            'publisher': ['test@example.com'],
            'date': ['2023-01-01']
        })
        data.to_csv('test_news.csv', index=False)
        
        df = load_news_data('test_news.csv')
        self.assertEqual(len(df), 1)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df['date']))
        
if __name__ == '__main__':
    unittest.main()