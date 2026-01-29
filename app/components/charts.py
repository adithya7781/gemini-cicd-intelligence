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
