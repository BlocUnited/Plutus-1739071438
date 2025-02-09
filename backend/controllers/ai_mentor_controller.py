from typing import Dict, Any, List, Optional
import os
from fastapi import APIRouter, HTTPException
from backend.services.ai_mentor_service import AIMentorService
from pydantic import BaseModel

router = APIRouter()
ai_mentor_service = AIMentorService()

class GenerateAIResponseRequest(BaseModel):
    userId: str
    prompt: str

@router.post("/ai/mentor", response_model=str)
async def generate_ai_response(request: GenerateAIResponseRequest):
    try:
        response = await ai_mentor_service.generate_ai_response(request.userId, request.prompt)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
