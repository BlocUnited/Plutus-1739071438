from typing import Dict, Any, List, Optional
import os
import uvicorn
from fastapi import FastAPI
from backend.config.config import Config
from backend.database.database import get_database
from backend.middleware.middleware import setup_middleware
from backend.routes.api_router import api_router

# Load global configuration
Config.log_config()

# Initialize FastAPI app
app = FastAPI()

# Setup middleware
setup_middleware(app)

# Register routes
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    # Initialize database connection
    await get_database()
    appLogger.info("Database connection established.")

@app.on_event("shutdown")
async def shutdown_event():
    # Close database connection if needed
    appLogger.info("Shutting down the application.")

if __name__ == '__main__':
    appLogger.info(f"Starting application on port 5000 with BACKEND_URL={os.environ.get('BACKEND_URL', 'Not Set')} and FRONTEND_URL={os.environ.get('FRONTEND_URL', 'Not Set')}")
    uvicorn.run(app, host="0.0.0.0", port=5000)