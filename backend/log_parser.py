def parse_log(text):

    error_count = text.count("ERROR")
    warning_count = text.count("WARNING")

    failed = False
    if "FAILED" in text or "Error:" in text:
        failed = True

    return {
        "error_count": error_count,
        "warning_count": warning_count,
        "failed": failed
    }
