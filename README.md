# Fraud Detection System

This project is a beginner-friendly real-time fraud detection system built with Python. It trains a machine learning model to detect suspicious transactions, serves predictions through a FastAPI API, and includes monitoring for data drift and alerting support.

## Features
- Fraud prediction API using FastAPI
- XGBoost-based model training
- Optional MLflow experiment tracking
- Data drift detection with Evidently
- Slack alert support for drift events
- Docker and CI workflow setup

## Project Structure
```text
fraud-detection-system/
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── drift_detector.py
│   └── mlflow_server.py
├── scripts/
├── tests/
├── Dockerfile
├── requirements.txt
├── README.md
└── GUIDE.md

Installation
pip install -r requirements.txt

Train the Model
python src/train.py

Run the API
uvicorn src.predict:app --reload

Example Prediction
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"transaction": {"time": 100, "v1": -1.2, "v2": 0.5, "amount": 150}}'

Drift Monitoring
python scripts/run_drift_check.py

Notes
This project uses a synthetic fallback dataset when the real credit card dataset is not available.

License
This project is for educational and demonstration purposes.

If you want, I can also give you a more polished version with badges, screenshots, and a cleaner professional layout.If you want, I can also give you a more polished version with badges, screenshots, and a cleaner professional layout.
