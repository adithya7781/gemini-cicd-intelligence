import streamlit as st

def summary_cards(total_runs, failed_runs, avg_errors, critical_count):

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Runs", total_runs)
    col2.metric("Failed Runs", failed_runs)
    col3.metric("Avg Errors", round(avg_errors, 2))
    col4.metric("Critical Alerts", critical_count)
    col5.metric("Severity Critical", severity_critical_count)


