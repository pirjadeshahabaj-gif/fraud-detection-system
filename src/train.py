"""
Train a fraud detection model using XGBoost
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import joblib
import os

def generate_synthetic_data(n_samples=1000):
    """Generate synthetic credit card transaction data"""
    np.random.seed(42)
    
    # Generate features
    data = {
        'Time': np.random.randint(0, 86400, n_samples),
        'Amount': np.random.exponential(100, n_samples),
    }
    
    # Add V1-V28 principal components (simulated)
    for i in range(1, 29):
        data[f'V{i}'] = np.random.normal(0, 1, n_samples)
    
    # Generate labels (5% fraud rate)
    fraud_indices = np.random.choice(n_samples, int(n_samples * 0.05), replace=False)
    labels = np.zeros(n_samples)
    labels[fraud_indices] = 1
    
    df = pd.DataFrame(data)
    df['Class'] = labels
    
    return df

def train_model():
    """Train XGBoost fraud detection model"""
    print("Loading data...")
    
    # Try to load real data, fallback to synthetic
    try:
        df = pd.read_csv('data/creditcard.csv')
        print(f"Loaded real data: {df.shape[0]} transactions")
    except FileNotFoundError:
        print("Real dataset not found, generating synthetic data...")
        df = generate_synthetic_data(n_samples=10000)
    
    print(f"Data shape: {df.shape}")
    
    # Prepare data
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    print("Training XGBoost model...")
    model = XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        random_state=42,
        eval_metric='logloss',
        verbosity=0
    )
    
    model.fit(X_train_scaled, y_train, verbose=False)
    
    # Evaluate
    train_score = model.score(X_train_scaled, y_train)
    test_score = model.score(X_test_scaled, y_test)
    
    print(f"\n✅ Model training completed!")
    print(f"Train Accuracy: {train_score:.4f}")
    print(f"Test Accuracy: {test_score:.4f}")
    
    # Save model and scaler
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/fraud_detection_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    
    print("✅ Model saved to: models/fraud_detection_model.pkl")
    print("✅ Scaler saved to: models/scaler.pkl")

if __name__ == "__main__":
    train_model()
