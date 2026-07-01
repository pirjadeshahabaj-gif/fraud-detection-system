"""
Run data drift detection
"""
from src.drift_detector import detect_drift
import pandas as pd
import numpy as np

def main():
    print("🔍 Running data drift detection...")
    
    # Generate reference data (training data distribution)
    np.random.seed(42)
    reference = pd.DataFrame({
        'V1': np.random.normal(0, 1, 1000),
        'V2': np.random.normal(0, 1, 1000),
        'Amount': np.random.exponential(100, 1000)
    })
    
    # Generate current data (with slight drift)
    current = pd.DataFrame({
        'V1': np.random.normal(0.5, 1.2, 1000),  # Shifted mean
        'V2': np.random.normal(0.3, 1.1, 1000),
        'Amount': np.random.exponential(120, 1000)  # Shifted scale
    })
    
    # Detect drift
    result = detect_drift(reference, current)
    
    if result:
        print("✅ Drift detection completed!")
        print(f"Result: {result}")
    else:
        print("⚠️  Drift detection skipped (Evidently not installed)")

if __name__ == "__main__":
    main()
