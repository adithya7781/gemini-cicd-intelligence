import streamlit as st
import plotly.express as px
import pandas as pd


def pipeline_status_chart(run_status):

    if not run_status:
        st.warning("No pipeline data to display")
        return

    df = pd.DataFrame(run_status)

    status_counts = (
        df["status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = ["status", "count"]

    fig = px.bar(
        status_counts,
        x="status",
        y="count",
        title="Pipeline Execution Status",
        template="plotly_dark"
    )

    st.plotly_chart(fig, width="stretch")

def error_trend_line_chart(metric_docs):

    if not metric_docs:
        st.warning("No metrics data available")
        return

    df = pd.DataFrame(metric_docs)

    if "timestamp" not in df.columns:
        st.warning("Timestamp missing for trend chart")
        return

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    fig = px.line(
        df,
        x="timestamp",
        y="error_count",
        title="Error Trend Over Time",
        markers=True,
        template="plotly_dark"
    )

    st.plotly_chart(fig, width="stretch")
