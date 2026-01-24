import streamlit as st

def summary_cards(total_runs, failed_runs, avg_errors):

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Pipeline Runs", total_runs)
    col2.metric("Failed Runs", failed_runs)
    col3.metric("Avg Errors / Run", round(avg_errors, 2))
