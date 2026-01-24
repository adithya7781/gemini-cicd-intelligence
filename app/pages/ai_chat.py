import streamlit as st
from services.mongo_client import runs, metrics
from services.gemini_client import ask_gemini

def render():

    st.title("🤖 Gemini CI/CD Assistant")

    query = st.text_input("Ask about your CI/CD pipeline")

    if st.button("Ask Gemini") and query:

        latest_run = runs.find_one(sort=[("_id", -1)])
        latest_metrics = metrics.find_one(sort=[("_id", -1)])

        if not latest_run or not latest_metrics:
            st.warning("No pipeline data available yet.")
            return

        context = f"""
Pipeline Status: {latest_run['status']}
Timestamp: {latest_run['timestamp']}

Errors: {latest_metrics['error_count']}
Warnings: {latest_metrics['warning_count']}
"""

        with st.spinner("Analyzing pipeline..."):
            response = ask_gemini(context, query)

        st.write(response)
