"""
FastAPI application for fraud detection predictions
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import numpy as np
from typing import Dict, Any

# Initialize FastAPI app
app = FastAPI(
    title="Fraud Detection API",
    description="Real-time fraud detection using XGBoost",
    version="1.0.0"
)

# Load model and scaler
MODEL_PATH = "models/fraud_detection_model.pkl"
SCALER_PATH = "models/scaler.pkl"

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("✅ Model and scaler loaded successfully")
except FileNotFoundError:
    print("⚠️  Warning: Model files not found. Run training first!")
    model = None
    scaler = None

# Request/Response models
class Transaction(BaseModel):
    time: float
    v1: float
    v2: float
    v3: float = 0.0
    v4: float = 0.0
    v5: float = 0.0
    v6: float = 0.0
    v7: float = 0.0
    v8: float = 0.0
    v9: float = 0.0
    v10: float = 0.0
    v11: float = 0.0
    v12: float = 0.0
    v13: float = 0.0
    v14: float = 0.0
    v15: float = 0.0
    v16: float = 0.0
    v17: float = 0.0
    v18: float = 0.0
    v19: float = 0.0
    v20: float = 0.0
    v21: float = 0.0
    v22: float = 0.0
    v23: float = 0.0
    v24: float = 0.0
    v25: float = 0.0
    v26: float = 0.0
    v27: float = 0.0
    v28: float = 0.0
    amount: float

class PredictionRequest(BaseModel):
    transaction: Transaction

class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    is_fraud: bool
    confidence: str
    message: str

# Routes
@app.get("/", tags=["Info"])
async def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to Fraud Detection API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health", tags=["Health"])
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.post("/predict", response_model=PredictionResponse, tags=["Predictions"])
async def predict(request: PredictionRequest) -> Dict[str, Any]:
    """
    Predict if a transaction is fraudulent
    
    Example request:
    {
        "transaction": {
            "time": 100,
            "v1": -1.2,
            "v2": 0.5,
            "amount": 150
        }
    }
    """
    
    if model is None or scaler is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please train the model first."
        )
    
    try:
        # Extract transaction data
        tx = request.transaction
        
        # Create feature vector in correct order
        features = np.array([[
            tx.time, tx.v1, tx.v2, tx.v3, tx.v4, tx.v5, tx.v6, tx.v7,
            tx.v8, tx.v9, tx.v10, tx.v11, tx.v12, tx.v13, tx.v14, tx.v15,
            tx.v16, tx.v17, tx.v18, tx.v19, tx.v20, tx.v21, tx.v22, tx.v23,
            tx.v24, tx.v25, tx.v26, tx.v27, tx.v28, tx.amount
        ]])
        
        # Scale features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0][int(prediction)]
        
        # Determine confidence level
        if probability > 0.9:
            confidence = "Very High"
        elif probability > 0.75:
            confidence = "High"
        elif probability > 0.6:
            confidence = "Medium"
        else:
            confidence = "Low"
        
        # Generate message
        if prediction == 1:
            message = f"⚠️  FRAUD ALERT! Transaction flagged as suspicious (confidence: {confidence})"
        else:
            message = f"✅ Transaction appears to be legitimate (confidence: {confidence})"
        
        return {
            "prediction": int(prediction),
            "probability": round(float(probability), 4),
            "is_fraud": bool(prediction == 1),
            "confidence": confidence,
            "message": message
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Prediction error: {str(e)}"
        )

@app.get("/stats", tags=["Info"])
async def stats():
    """Get model statistics"""
    return {
        "model_name": "XGBoost Fraud Detector",
        "version": "1.0.0",
        "features": 30,
        "model_loaded": model is not None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
