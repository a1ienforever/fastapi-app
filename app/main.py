import uvicorn
from fastapi import FastAPI

from app.handlers import main_router

app = FastAPI()

app.include_router(main_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
