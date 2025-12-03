from fastapi import FastAPI
from app.api.routes import api_router

app= FastAPI(title= "Clinical Trials API")

app.include_router(api_router)