from typing import Dict, Any, List, Optional
import os
from fastapi import HTTPException
from backend.models.ai_mentor import AIMentorModel
from backend.database.database import get_database
import openai

class AIMentorService:
    """Service class for AI mentor-related operations."""

    async def generate_ai_response(self, userId: str, prompt: str) -> str:
        db = await get_database()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        ai_response = response['choices'][0]['message']['content']
        ai_mentor = AIMentorModel(
            userId=userId,
            prompt=prompt,
            response=ai_response,
            createdAt=datetime.utcnow()
        )
        await db["AiMentor"].insert_one(ai_mentor.dict(by_alias=True))
        return ai_response
