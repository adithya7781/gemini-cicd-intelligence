import streamlit as st
import pandas as pd


def show_runs_table(run_data):
    st.subheader("📄 Pipeline Runs")

    if not run_data:
        st.info("No run records available.")
        return

    df = pd.DataFrame(run_data)

    st.dataframe(
        df,
        use_container_width=True,
        height=350
    )
