from sklearn.ensemble import IsolationForest
import numpy as np

# ------------------------------
# Severity Score Calculation
# ------------------------------

def calculate_severity(error_count, warning_count):

    score = (error_count * 2) + warning_count

    if score <= 2:
        level = "Low"
    elif score <= 6:
        level = "Medium"
    else:
        level = "Critical"

    return score, level


# ------------------------------
# Lightweight Rule-Based Anomaly
# (Fast + Research Friendly)
# ------------------------------

def detect_anomaly(error_count, warning_count):

    # Simple statistical heuristic (better than broken ML on single sample)

    if error_count >= 4 or warning_count >= 6:
        return "Anomaly"

    return "Normal"


# ------------------------------
# Critical Alert Detection
# ------------------------------

def detect_critical_alert(error_count, warning_count, logs_text):

    critical = False
    reasons = []

    logs_upper = logs_text.upper()

    # High error volume
    if error_count >= 3:
        critical = True
        reasons.append("High error volume")

    # Pipeline failure keywords
    if "FAILED" in logs_upper:
        critical = True
        reasons.append("Pipeline failure detected")

    if "EXIT CODE 1" in logs_upper:
        critical = True
        reasons.append("Non-zero exit code")

    if "BUILD FAILED" in logs_upper:
        critical = True
        reasons.append("Build failed")

    return critical, reasons
