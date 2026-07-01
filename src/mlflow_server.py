"""
MLflow experiment tracking setup
"""
import mlflow
import os

def setup_mlflow():
    """Setup MLflow tracking"""
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("fraud-detection")
    print("✅ MLflow tracking configured")

def log_model_metrics(accuracy, precision, recall, f1):
    """Log model metrics to MLflow"""
    with mlflow.start_run():
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)
        print("✅ Metrics logged to MLflow")

if __name__ == "__main__":
    setup_mlflow()
