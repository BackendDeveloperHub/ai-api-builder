import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODELS = [
    "gemini-2.0-flash",
    "gemini-1.5-pro",
    "gemini-1.5-flash",
]

def generate_api(prompt: str) -> str:
    response = client.models.generate_content(model=MODELS[0], contents=f"""Generate a complete FastAPI endpoint.
User request: {prompt}
Return ONLY raw Python code. No markdown, no explanation.""")
    code = response.text.strip()
    return code