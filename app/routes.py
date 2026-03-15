from fastapi import APIRouter
from agent import generate_api
from pydantic import BaseModel

router = APIRouter()
class PromptRequest(BaseModel):
    prompt: str
@router.post("/generate-api")
def create_api(request: PromptRequest):
    api_code = generate_api(request.prompt)
    return {"api_code": api_code}