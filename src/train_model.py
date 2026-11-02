import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

class ThermalModelTrainer:
    def __init__(self):
        # Using Random Forest to capture complex thermodynamic non-linear relationships
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train(self, X_train, y_train):
        """Trains the AI framework on historical engine thermal properties."""
        self.model.fit(X_train, y_train)
        print("Model training completed successfully.")

    def evaluate(self, X_test, y_test):
        """Validates AI predictions against ground-truth simulation solvers."""
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        print(f"Validation Metrics -> Mean Squared Error: {mse:.4f}, R2 Score: {r2:.4f}")
        return r2

    def save_model(self, output_path):
        """Serializes the trained asset for production inference deployment."""
        joblib.dump(self.model, output_path)
        print(f"Model saved to {output_path}")
      
