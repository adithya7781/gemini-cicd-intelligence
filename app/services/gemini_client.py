from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-flash-latest"


def ask_gemini(context, query):

    prompt = f"""
You are a DevOps AI assistant.

Pipeline context:
{context}

User question:
{query}

Give concise root cause analysis and improvement suggestions.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
