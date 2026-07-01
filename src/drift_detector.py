"""
Data drift detection using Evidently
"""
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import pandas as pd
import numpy as np

def detect_drift(reference_data: pd.DataFrame, current_data: pd.DataFrame):
    """
    Detect data drift between reference and current datasets
    """
    try:
        from evidently.report import Report
        from evidently.metric_preset import DataDriftPreset
        
        report = Report(metrics=[DataDriftPreset()])
        report.run(reference_data=reference_data, current_data=current_data)
        
        return report.as_dict()
    except ImportError:
        print("⚠️  Evidently not installed. Install with: pip install evidently")
        return None

if __name__ == "__main__":
    print("Drift detection module loaded")
