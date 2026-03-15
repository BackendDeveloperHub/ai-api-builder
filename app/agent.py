import os
from dotenv import load_dotenv
from google import genai
from fastapi import HTTPException

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODELS = [
    "gemini-2.0-flash",
    "gemini-1.5-pro",
    "gemini-1.5-flash",
]

def generate_api(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODELS[1],  # Use the first model as a fallback
        contents=f"""Generate a complete FastAPI endpoint.
User request: {prompt}
Return ONLY raw Python code. No markdown, no explanation."""
    )
    code = response.text.strip()
    # Strip markdown fences if Gemini adds them
    if code.startswith("```"):
        code = code.split("\n", 1)[1]
        code = code.rsplit("```", 1)[0]
    return code