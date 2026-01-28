import streamlit as st
import pandas as pd


def show_runs_table(data):

    df = pd.DataFrame(data)

    st.subheader("Pipeline Metrics Summary")

    st.dataframe(df, use_container_width=True)
