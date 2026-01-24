import streamlit as st
from services.mongo_client import runs, metrics
from components.cards import summary_cards
from components.charts import pipeline_status_chart
from components.tables import show_runs_table


def render():

    st.title("📊 CI/CD Observability Dashboard")

    total_runs = runs.count_documents({})
    failed_runs = runs.count_documents({"status": "failed"})

    metric_docs = list(metrics.find())

    if total_runs == 0:
        st.warning("No pipeline runs found.")
        return

    avg_errors = (
        sum([m["error_count"] for m in metric_docs]) / len(metric_docs)
        if metric_docs else 0
    )

    summary_cards(total_runs, failed_runs, avg_errors)

    run_data = list(runs.find({}, {"_id": 0, "status": 1}))
    pipeline_status_chart(run_data)
    show_runs_table(run_data)
