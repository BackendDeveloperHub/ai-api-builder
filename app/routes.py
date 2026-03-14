from fastapi import APIRouter
from app.agent import generate_api

router = APIRouter()

@router.post("/generate-api")
def create_api(prompt: str):
    code = generate_api(prompt)
    return {"generated_code": code}
