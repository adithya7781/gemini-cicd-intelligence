from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["cicd_ai"]

# Collections
runs = db.pipeline_runs
logs = db.logs
metrics = db.metrics
telemetry = db.telemetry
