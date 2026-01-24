import streamlit as st
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)

from backend.log_ingestor import ingest_log


def render():

    st.title("📤 Upload CI/CD Log")

    file = st.file_uploader("Upload pipeline log file", type=["log", "txt"])

    if file:

        save_path = "data/samples/uploaded.log"

        with open(save_path, "wb") as f:
            f.write(file.read())

        ingest_log(save_path)

        st.success("Log uploaded and processed successfully.")
