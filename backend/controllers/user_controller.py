from typing import Dict, Any, List, Optional
import os
from fastapi import APIRouter, HTTPException, Depends
from backend.services.user_service import UserService
from backend.models.user import UserModel
from pydantic import BaseModel

router = APIRouter()
user_service = UserService()

class RegisterUserRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginUserRequest(BaseModel):
    email: str
    password: str

class UpdateProfileRequest(BaseModel):
    profile: dict

@router.post("/users/register", response_model=UserModel)
async def register_user(request: RegisterUserRequest):
    try:
        user = await user_service.register_user(request.email, request.username, request.password)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/users/login", response_model=str)
async def login_user(request: LoginUserRequest):
    try:
        token = await user_service.login_user(request.email, request.password)
        return token
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/users/profile", response_model=UserModel)
async def update_user_profile(userId: str, request: UpdateProfileRequest):
    try:
        updated_user = await user_service.update_profile(userId, request.profile)
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
