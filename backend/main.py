from backend.log_ingestor import ingest_log

if __name__ == "__main__":

    test_file = "data/samples/demo_logs.log"

    ingest_log(test_file)
