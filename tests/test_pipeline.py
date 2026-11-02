import unittest
import numpy as np
import pandas as pd
import os
from src.data_pipeline import EngineDataPipeline

class TestEnginePipeline(unittest.TestCase):
    def setUp(self):
        self.dummy_path = 'data/test_sample.csv'
        df = pd.DataFrame({
            'engine_rpm':,
            'fuel_air_ratio': [14.7, 13.5],
            'coolant_flow_rate': [1.5, 2.0],
            'ambient_temp':,
            'cylinder_head_temp_celsius': [180.0, 205.0]
        })
        os.makedirs('data', exist_ok=True)
        df.to_csv(self.dummy_path, index=False)

    def test_pipeline_extraction(self):
        pipeline = EngineDataPipeline(self.dummy_path)
        df = pipeline.load_and_clean_data()
        X, y = pipeline.extract_features(df)
        self.assertEqual(X.shape, (2, 4))
        self.assertEqual(len(y), 2)

    def tearDown(self):
        if os.path.exists(self.dummy_path):
            os.remove(self.dummy_path)

if __name__ == '__main__':
    unittest.main()
  
