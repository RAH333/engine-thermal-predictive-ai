import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class EngineDataPipeline:
    def __init__(self, filepath):
        self.filepath = filepath
        self.scaler = StandardScaler()

    def load_and_clean_data(self):
        """Loads physical engine simulation parameters and handles missing values."""
        df = pd.read_csv(self.filepath)
        # Drop rows with anomalies or null physical states
        df = df.dropna()
        return df

    def extract_features(self, df):
        """Engineering domain feature scaling: Splits features from target variables."""
        X = df[['engine_rpm', 'fuel_air_ratio', 'coolant_flow_rate', 'ambient_temp']]
        y = df['cylinder_head_temp_celsius']
        
        # Scale features to balance different physical metric units (RPM vs Ratio)
        X_scaled = self.scaler.fit_transform(X)
        return X_scaled, y

    def split_dataset(self, X, y):
        """Prepares train and validation sets for model verification."""
        return train_test_split(X, y, test_size=0.2, random_state=42)
      
