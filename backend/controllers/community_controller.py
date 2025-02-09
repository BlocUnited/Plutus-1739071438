from typing import Dict, Any, List, Optional
import os
from fastapi import APIRouter, HTTPException
from backend.services.community_service import CommunityService
from backend.models.community import CommunityModel
from pydantic import BaseModel

router = APIRouter()
community_service = CommunityService()

class CreateCommunityRequest(BaseModel):
    name: str
    description: str

@router.post("/communities", response_model=CommunityModel)
async def create_community(request: CreateCommunityRequest):
    try:
        community = await community_service.create_community(request.name, request.description)
        return community
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/communities/{communityId}/join")
async def join_community(userId: str, communityId: str):
    try:
        community = await community_service.join_community(userId, communityId)
        return community
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
