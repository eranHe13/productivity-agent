from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
from app.ai.coach_chain import run_coach
from app.core.security import rate_limiter

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str = Field(..., min_length=3, max_length=500)

    @validator("prompt")
    def no_empty(cls, v):
        if not v.strip():
            raise ValueError("Prompt cannot be empty")
        return v

@router.post("/")
def ask_coach(data: PromptRequest):
    rate_limiter.check()
    answer = run_coach(data.prompt)
    return {"answer": answer}
