from app.services.mongo_client import metrics


def get_average_errors():

    data = list(metrics.find())

    if not data:
        return 0

    total = sum([m["error_count"] for m in data])
    return total / len(data)
