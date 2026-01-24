from datetime import datetime
import uuid

from backend.log_parser import parse_log
from backend.mongo_client import runs, logs, metrics


def ingest_log(file_path):

    with open(file_path, "r", errors="ignore") as f:
        content = f.read()

    parsed = parse_log(content)

    run_id = str(uuid.uuid4())

    runs.insert_one({
        "run_id": run_id,
        "status": "failed" if parsed["failed"] else "success",
        "timestamp": datetime.utcnow()
    })

    logs.insert_one({
        "run_id": run_id,
        "log_text": content,
        "timestamp": datetime.utcnow()
    })

    metrics.insert_one({
        "run_id": run_id,
        "error_count": parsed["error_count"],
        "warning_count": parsed["warning_count"]
    })

    print("Pipeline log ingested:", run_id)
