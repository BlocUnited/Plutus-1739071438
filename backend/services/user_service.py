from typing import Dict, Any, List, Optional
import os
import bcrypt
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from backend.models.user import UserModel
from backend.database.database import get_database

class UserService:
    """Service class for user-related operations."""

    async def register_user(self, email: str, username: str, password: str) -> UserModel:
        db = await get_database()
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = UserModel(
            username=username,
            email=email,
            passwordHash=hashed_password,
            createdAt=datetime.utcnow(),
            updatedAt=datetime.utcnow()
        )
        await db["Users"].insert_one(user.dict(by_alias=True))
        return user

    async def login_user(self, email: str, password: str) -> str:
        db = await get_database()
        user = await db["Users"].find_one({"email": email})
        if user is None:
            raise HTTPException(status_code=400, detail="Invalid email or password")
        if not bcrypt.checkpw(password.encode(), user["passwordHash"].encode()):
            raise HTTPException(status_code=400, detail="Invalid email or password")
        token = jwt.encode({"sub": str(user["_id"]), "exp": datetime.utcnow() + timedelta(hours=1)}, "SECRET_KEY")
        return token

    async def update_profile(self, userId: str, profileData: dict) -> UserModel:
        db = await get_database()
        updated_user = await db["Users"].find_one_and_update(
            {"_id": userId},
            {"$set": {"profile": profileData, "updatedAt": datetime.utcnow()}},
            return_document=True
        )
        if updated_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return UserModel(**updated_user)
