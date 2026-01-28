from sklearn.ensemble import IsolationForest
import numpy as np


def calculate_severity(error_count, warning_count):

    score = (error_count * 2) + warning_count

    if score <= 2:
        level = "Low"
    elif score <= 6:
        level = "Medium"
    else:
        level = "Critical"

    return score, level


def detect_anomaly(error_count, warning_count):

    X = np.array([[error_count, warning_count]])

    model = IsolationForest(contamination=0.2)
    model.fit(X)

    result = model.predict(X)

    return "Anomaly" if result[0] == -1 else "Normal"
