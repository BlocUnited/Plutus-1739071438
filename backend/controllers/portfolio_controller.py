from typing import Dict, Any, List, Optional
import os
from fastapi import APIRouter, HTTPException
from backend.services.portfolio_service import PortfolioService
from backend.models.portfolio import PortfolioModel
from pydantic import BaseModel

router = APIRouter()
portfolio_service = PortfolioService()

class CreatePortfolioRequest(BaseModel):
    userId: str
    title: str
    description: str

class GetPortfolioResponse(PortfolioModel):
    pass

@router.post("/portfolios", response_model=PortfolioModel)
async def create_portfolio(request: CreatePortfolioRequest):
    try:
        portfolio = await portfolio_service.create_portfolio(request.userId, request.title, request.description)
        return portfolio
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/portfolios/{portfolioId}", response_model=GetPortfolioResponse)
async def get_portfolio(portfolioId: str):
    try:
        portfolio = await portfolio_service.get_portfolio(portfolioId)
        return portfolio
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/portfolios/{portfolioId}/like")
async def like_portfolio(portfolioId: str, userId: str):
    try:
        likes = await portfolio_service.like_portfolio(portfolioId, userId)
        return {"likes": likes}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
