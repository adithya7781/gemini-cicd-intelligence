import streamlit as st
import plotly.express as px
import pandas as pd

def pipeline_status_chart(run_data):

    df = pd.DataFrame(run_data)

    fig = px.histogram(
        df,
        x="status",
        title="Pipeline Run Status Distribution",
        template="plotly_dark"
    )

    st.plotly_chart(fig, width="stretch")
