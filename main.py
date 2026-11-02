import os
from src.data_pipeline import EngineDataPipeline
from src.train_model import ThermalModelTrainer
from src.inference_engine import EngineInferenceEngine

def main():
    data_path = os.path.join('data', 'raw_simulation_data.csv')
    model_path = os.path.join('models', 'thermal_predictor_model.pkl')

    print("=== [Step 1] Initializing Engine Data Pipeline ===")
    pipeline = EngineDataPipeline(data_path)
    df = pipeline.load_and_clean_data()
    X, y = pipeline.extract_features(df)
    X_train, X_test, y_train, y_test = pipeline.split_dataset(X, y)

    print("\n=== [Step 2] Training Thermal AI Predictor ===")
    trainer = ThermalModelTrainer()
    trainer.train(X_train, y_train)
    trainer.evaluate(X_test, y_test)
    
    # Ensure directory exists before saving
    os.makedirs('models', exist_ok=True)
    trainer.save_model(model_path)

    print("\n=== [Step 3] Running Production Inference Simulation ===")
    inference = EngineInferenceEngine(model_path)
    
    # Simulating a high-load scenario: 4500 RPM, 12.8 Fuel-Air Ratio, 2.8 L/min Coolant, 32C Ambient
    sample_engine_state = [4500, 12.8, 2.8, 32]
    predicted_head_temp = inference.predict_temperature(sample_engine_state)
    
    print(f"Input Operational Parameters: RPM={sample_engine_state[0]}, AFR={sample_engine_state[1]}")
    print(f"👉 Predicted Steady-State Cylinder Head Temp: {predicted_head_temp:.2f}°C")

if __name__ == '__main__':
    main()
