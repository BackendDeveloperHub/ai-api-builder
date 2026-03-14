import google.generativeai as genai
import os

# Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_api(user_prompt: str):

    prompt = f"""
You are an expert backend developer.

Generate a FastAPI CRUD API based on this requirement:

{user_prompt}

Rules:
- Use FastAPI
- Create routes
- Create Pydantic models
- Simple in-memory storage
- Return only Python code
"""

    response = model.generate_content(prompt)

    return response.text
