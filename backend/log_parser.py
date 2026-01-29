import pandas as pd
import json
import PyPDF2


def extract_pdf_text(file_path):

    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text


def parse_log(file_path):

    error_count = 0
    warning_count = 0

    ext = file_path.split(".")[-1].lower()

    # ---------- TXT / LOG ----------
    if ext in ["log", "txt"]:

        with open(file_path, "r", errors="ignore") as f:
            lines = f.readlines()

    # ---------- CSV ----------
    elif ext == "csv":

        df = pd.read_csv(file_path)
        lines = df.astype(str).values.flatten().tolist()

    # ---------- Excel ----------
    elif ext == "xlsx":

        df = pd.read_excel(file_path)
        lines = df.astype(str).values.flatten().tolist()

    # ---------- JSON ----------
    elif ext == "json":

        with open(file_path) as f:
            data = json.load(f)

        lines = json.dumps(data).split(",")

    # ---------- PDF ----------
    elif ext == "pdf":

        text = extract_pdf_text(file_path)
        lines = text.split("\n")

    else:
        raise ValueError("Unsupported file format")

    # ---------- Count errors and warnings ----------
    for line in lines:

        text = str(line).strip().lower()

        # Strict ERROR detection
        if text.startswith("error") or " error " in text:
            error_count += 1

        # Strict WARNING detection
        if text.startswith("warn") or text.startswith("warning") or " warning " in text:
            warning_count += 1

    return {
        "error_count": error_count,
        "warning_count": warning_count,
        "full_text": "\n".join(map(str, lines))
    }
