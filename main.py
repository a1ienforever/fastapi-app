


import uvicorn
from fastapi import FastAPI

from model import CountrySchema

app = FastAPI()
countries = []
flag = True


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/countries")
async def add_country(country: CountrySchema):
    countries.append(country)
    return {"status": "OK", "country": country}


@app.get("/countries")
async def list_countries() -> list[CountrySchema]:
    return countries


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
