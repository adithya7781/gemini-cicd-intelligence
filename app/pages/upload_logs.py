import streamlit as st
import sys
import os
import uuid

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)

from backend.log_ingestor import ingest_log


def render():

    st.title("📤 Upload CI/CD Logs")

    uploaded_file = st.file_uploader(
        "Upload pipeline log file",
        type=["log", "txt", "csv", "xlsx", "pdf", "json"]
    )

    if uploaded_file:

        os.makedirs("data/uploads", exist_ok=True)

        file_extension = uploaded_file.name.split(".")[-1]

        unique_name = f"{uuid.uuid4()}.{file_extension}"

        save_path = os.path.join("data/uploads", unique_name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())

        if st.button("Process Log File"):

            with st.spinner("Parsing and storing log data..."):
                run_id = ingest_log(save_path)

            st.success("Log uploaded and processed successfully")
            st.code(run_id)
