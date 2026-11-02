import joblib
import numpy as np

class EngineInferenceEngine:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict_temperature(self, raw_input_features):
        """Predicts real-time engine thermal state based on dynamic operational loads.
        
        Args:
            raw_input_features (list): [engine_rpm, fuel_air_ratio, coolant_flow_rate, ambient_temp]
        """
        input_data = np.array(raw_input_features).reshape(1, -1)
        # In production, ensure data passes through the scaled transformation vector
        predicted_temp = self.model.predict(input_data)
        return predicted_temp[0]
      
