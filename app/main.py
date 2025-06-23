import uvicorn
from fastapi import FastAPI

from app.handlers import routers

app = FastAPI()

for router in routers:
    app.include_router(router)
countries = []
flag = True



@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True, env_file='../.env')
