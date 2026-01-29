import uuid
from backend.log_parser import parse_log
from backend.metrics_engine import calculate_severity, detect_anomaly, detect_critical_alert
from backend.mongo_client import runs, logs, metrics


def ingest_log(file_path):

    parsed = parse_log(file_path)

    error_count = parsed["error_count"]
    warning_count = parsed["warning_count"]
    full_text = parsed["full_text"]

    severity_score, severity_level = calculate_severity(error_count, warning_count)

    anomaly_status = detect_anomaly(error_count, warning_count)

    run_id = str(uuid.uuid4())

    status = "failed" if error_count > 0 else "success"

    # Store pipeline run
    runs.insert_one({
        "run_id": run_id,
        "status": status
    })

    # Store raw log stats
    logs.insert_one({
        "run_id": run_id,
        "error_count": error_count,
        "warning_count": warning_count
    })

    # Store computed metrics
    metrics.insert_one({
        "run_id": run_id,
        "error_count": error_count,
        "warning_count": warning_count,
        "severity_score": severity_score,
        "severity_level": severity_level,
        "anomaly_status": anomaly_status
    })

    return run_id

