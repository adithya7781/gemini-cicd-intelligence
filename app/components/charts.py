import streamlit as st
import pandas as pd
import plotly.express as px


def pipeline_status_chart(run_data):

    df = pd.DataFrame(run_data)

    status_counts = df["status"].value_counts().reset_index()
    status_counts.columns = ["status", "count"]

    fig = px.bar(
        status_counts,
        x="status",
        y="count",
        title="Pipeline Run Status",
        template="plotly_dark"
    )

    st.plotly_chart(fig, width="stretch")

