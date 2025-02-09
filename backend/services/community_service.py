from typing import Dict, Any, List, Optional
import os
from fastapi import HTTPException
from backend.models.community import CommunityModel
from backend.database.database import get_database

class CommunityService:
    """Service class for community-related operations."""

    async def create_community(self, name: str, description: str) -> CommunityModel:
        db = await get_database()
        community = CommunityModel(
            name=name,
            description=description,
            createdAt=datetime.utcnow()
        )
        await db["Communities"].insert_one(community.dict(by_alias=True))
        return community

    async def join_community(self, userId: str, communityId: str) -> CommunityModel:
        db = await get_database()
        community = await db["Communities"].find_one_and_update(
            {"_id": communityId},
            {"$addToSet": {"members": userId}}
        )
        if community is None:
            raise HTTPException(status_code=404, detail="Community not found")
        return CommunityModel(**community)
