# 🚀 Fraud Detection System

A beginner-friendly, production-ready real-time fraud detection system built with Python, Machine Learning, and FastAPI. This project demonstrates how to build, train, and deploy an ML model for detecting fraudulent credit card transactions.

**Live Demo Available:** Visit `/docs` endpoint after starting the server for interactive API testing.

---

## 📋 Table of Contents
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Quick Start Guide](#-quick-start-guide)
- [Installation](#-installation)
- [Training the Model](#-training-the-model)
- [Running the API](#-running-the-api)
- [Testing the Predictions](#-testing-the-predictions)
- [Monitoring & Drift Detection](#-monitoring--drift-detection)
- [Docker Deployment](#-docker-deployment)
- [API Endpoints](#-api-endpoints)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

---

## ✨ Features

✅ **XGBoost-based Fraud Detection** - High-accuracy machine learning model  
✅ **FastAPI REST API** - Easy-to-use endpoints with automatic documentation  
✅ **Real-time Predictions** - Get fraud predictions in milliseconds  
✅ **Data Drift Detection** - Monitor model performance with Evidently  
✅ **Slack Alerts** - Get notified when data drift is detected  
✅ **MLflow Integration** - Track experiments and model metrics  
✅ **Docker Ready** - One-command deployment  
✅ **Synthetic Data Support** - Works without real dataset  
✅ **Production-Grade** - Error handling, logging, health checks  

---

## 📁 Project Structure

```
fraud-detection-system/
│
├── src/                          # Source code
│   ├── __init__.py              # Package initialization
│   ├── train.py                 # 🧠 Model training script
│   ├── predict.py               # 🔮 FastAPI prediction server
│   ├── drift_detector.py         # 📊 Data drift detection
│   └── mlflow_server.py          # 📈 MLflow experiment tracking
│
├── scripts/                      # Utility scripts
│   └── run_drift_check.py        # Run drift monitoring
│
├── models/                       # Trained models (auto-created)
│   ├── fraud_detection_model.pkl # Trained XGBoost model
│   └── scaler.pkl               # Feature scaler
│
├── data/                         # Dataset directory (optional)
│   └── creditcard.csv           # Credit card transaction data
│
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── .gitignore                   # Git ignore rules
├── README.md                    # This file
└── GUIDE.md                     # Detailed configuration guide
```

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.8 or higher** ([Download here](https://www.python.org/downloads/))
- **Git** ([Download here](https://git-scm.com/))
- **pip** (comes with Python)

### One-Minute Setup

```bash
# 1. Clone the repository
git clone https://github.com/pirjadeshahabaj-gif/fraud-detection-system.git
cd fraud-detection-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model
python src/train.py

# 4. Run the API (in terminal window)
uvicorn src.predict:app --reload

# 5. Test in another terminal
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"transaction": {"time": 100, "v1": -1.2, "v2": 0.5, "amount": 150}}'
```

---

## 📦 Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/pirjadeshahabaj-gif/fraud-detection-system.git
cd fraud-detection-system
```

### Step 2: Create Virtual Environment (Optional but Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**What gets installed:**
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `xgboost` - ML model
- `scikit-learn` - Data preprocessing
- `pandas` - Data handling
- `numpy` - Numerical computing
- `evidently` - Drift detection
- `mlflow` - Experiment tracking

---

## 🧠 Training the Model

### Run Training
```bash
python src/train.py
```

### Expected Output
```
Loading data...
Real dataset not found, generating synthetic data...
Data shape: (10000, 29)
Training XGBoost model...

✅ Model training completed!
Train Accuracy: 0.9856
Test Accuracy: 0.9823

✅ Model saved to: models/fraud_detection_model.pkl
✅ Scaler saved to: models/scaler.pkl
```

### What It Does
1. **Loads Data** - Uses real credit card data if available, otherwise generates synthetic data
2. **Preprocesses** - Splits into train/test sets (80/20 split)
3. **Scales Features** - Normalizes data for better model performance
4. **Trains Model** - XGBoost classifier with optimized parameters
5. **Saves Model** - Stores model and scaler for predictions

### Customization

Edit `src/train.py` to change:
- `n_samples` - Amount of synthetic data (default: 10,000)
- `n_estimators` - Number of trees (default: 100)
- `max_depth` - Tree depth (default: 5)
- `learning_rate` - Training speed (default: 0.1)

---

## 🔮 Running the API

### Start the Server

**Windows PowerShell:**
```powershell
uvicorn src.predict:app --reload
```

**macOS/Linux Terminal:**
```bash
uvicorn src.predict:app --reload
```

### Expected Output
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Server Features
- **Auto-reload** - Changes to code reload automatically (perfect for development)
- **Interactive Docs** - Available at http://127.0.0.1:8000/docs
- **Health Checks** - Check model status anytime
- **Error Handling** - Graceful error messages

### Stop the Server
Press `CTRL + C` in the terminal

---

## 🧪 Testing the Predictions

### Method 1: Using cURL (Command Line)

**Windows PowerShell:**
```powershell
$body = @{
    transaction = @{
        time = 100
        v1 = -1.2
        v2 = 0.5
        v3 = 2.0
        amount = 150
    }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/predict" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body
```

**macOS/Linux (bash):**
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "transaction": {
      "time": 100,
      "v1": -1.2,
      "v2": 0.5,
      "v3": 2.0,
      "amount": 150
    }
  }'
```

### Expected Response
```json
{
  "prediction": 0,
  "probability": 0.9234,
  "is_fraud": false,
  "confidence": "High",
  "message": "✅ Transaction appears to be legitimate (confidence: High)"
}
```

---

### Method 2: Interactive API Documentation

1. **Start the server** (see Running the API section)
2. **Open in browser:** http://127.0.0.1:8000/docs
3. **Click on `/predict` endpoint**
4. **Click "Try it out"**
5. **Modify the request body** with your transaction data
6. **Click "Execute"** to get prediction

### Method 3: Python Script

**Create `test_api.py`:**
```python
import requests
import json

URL = "http://127.0.0.1:8000/predict"

transaction_data = {
    "transaction": {
        "time": 100,
        "v1": -1.2,
        "v2": 0.5,
        "v3": 2.0,
        "v4": -0.7,
        "v5": 0.3,
        "v6": 0.0,
        "v7": 0.0,
        "v8": 0.0,
        "v9": 0.0,
        "v10": 0.0,
        "v11": 0.0,
        "v12": 0.0,
        "v13": 0.0,
        "v14": 0.0,
        "v15": 0.0,
        "v16": 0.0,
        "v17": 0.0,
        "v18": 0.0,
        "v19": 0.0,
        "v20": 0.0,
        "v21": 0.0,
        "v22": 0.0,
        "v23": 0.0,
        "v24": 0.0,
        "v25": 0.0,
        "v26": 0.0,
        "v27": 0.0,
        "v28": 0.0,
        "amount": 150
    }
}

response = requests.post(URL, json=transaction_data)
print(json.dumps(response.json(), indent=2))
```

**Run it:**
```bash
python test_api.py
```

---

## 📊 Monitoring & Drift Detection

### Run Drift Detection
```bash
python scripts/run_drift_check.py
```

### What It Does
- **Compares** current transaction patterns with training data
- **Detects** unusual changes in data distribution
- **Alerts** when model might need retraining
- **Logs** drift metrics for analysis

### Output
```
🔍 Running data drift detection...
✅ Drift detection completed!
Result: {...}
```

---

## 🐳 Docker Deployment

### Build Docker Image
```bash
docker build -t fraud-detection:latest .
```

### Run Docker Container
```bash
docker run -p 8000:8000 fraud-detection:latest
```

### Access API
Open browser to: http://localhost:8000/docs

---

## 📡 API Endpoints

### 1. **Root Endpoint** (Welcome)
```
GET /
```
**Response:**
```json
{
  "message": "Welcome to Fraud Detection API",
  "docs": "/docs",
  "version": "1.0.0"
}
```

---

### 2. **Health Check**
```
GET /health
```
**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

---

### 3. **Make Prediction** ⭐ Main Endpoint
```
POST /predict
```

**Request Body:**
```json
{
  "transaction": {
    "time": 100,
    "v1": -1.2,
    "v2": 0.5,
    "v3": 2.0,
    "amount": 150,
    "v4": 0.0,
    "v5": 0.0,
    "v6": 0.0,
    "v7": 0.0,
    "v8": 0.0,
    "v9": 0.0,
    "v10": 0.0,
    "v11": 0.0,
    "v12": 0.0,
    "v13": 0.0,
    "v14": 0.0,
    "v15": 0.0,
    "v16": 0.0,
    "v17": 0.0,
    "v18": 0.0,
    "v19": 0.0,
    "v20": 0.0,
    "v21": 0.0,
    "v22": 0.0,
    "v23": 0.0,
    "v24": 0.0,
    "v25": 0.0,
    "v26": 0.0,
    "v27": 0.0,
    "v28": 0.0
  }
}
```

**Response:**
```json
{
  "prediction": 0,
  "probability": 0.9234,
  "is_fraud": false,
  "confidence": "High",
  "message": "✅ Transaction appears to be legitimate (confidence: High)"
}
```

---

### 4. **Model Statistics**
```
GET /stats
```
**Response:**
```json
{
  "model_name": "XGBoost Fraud Detector",
  "version": "1.0.0",
  "features": 30,
  "model_loaded": true
}
```

---

## 🔧 Troubleshooting

### Problem: `ModuleNotFoundError: No module named 'fastapi'`
**Solution:**
```bash
pip install -r requirements.txt
```

### Problem: `Unable to connect to the remote server`
**Solution:** The API server is not running. Open a new terminal and run:
```bash
uvicorn src.predict:app --reload
```

### Problem: `FileNotFoundError: models/fraud_detection_model.pkl`
**Solution:** Train the model first:
```bash
python src/train.py
```

### Problem: Port 8000 already in use
**Solution:** Use a different port:
```bash
uvicorn src.predict:app --reload --port 8001
```

### Problem: Permission Denied (macOS/Linux)
**Solution:** Make scripts executable:
```bash
chmod +x src/train.py
chmod +x src/predict.py
```

---

## 📚 Learning Resources

- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **XGBoost Docs:** https://xgboost.readthedocs.io/
- **Scikit-learn:** https://scikit-learn.org/
- **Pandas:** https://pandas.pydata.org/

---

## 🤝 Contributing

Found a bug? Have a suggestion? Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📝 License

This project is for **educational and demonstration purposes**.

---

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the GUIDE.md for detailed configuration
- Review the code comments for implementation details

---

## 🎯 What's Next?

- [ ] Deploy to AWS/GCP/Azure
- [ ] Add more evaluation metrics
- [ ] Implement real-time monitoring dashboard
- [ ] Add model versioning
- [ ] Create production CI/CD pipeline
- [ ] Add authentication to API
- [ ] Implement rate limiting

---

**Made by the shahabaj pirjade**

**Last Updated:** July 1, 2026  
**Version:** 1.0.0  
**Status:** ✅ Production Ready
