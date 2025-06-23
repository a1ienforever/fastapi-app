from pydantic import BaseModel, Field

from app.schemas.country import CountrySchema


class CreatorSchema(BaseModel):
    name: str = Field(max_length=25)
    country: CountrySchema | None
