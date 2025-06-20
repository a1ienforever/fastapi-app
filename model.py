
from pydantic import BaseModel, ConfigDict, Field


class CountrySchema(BaseModel):
    name: str = Field(max_length=25)

    model_config = ConfigDict(extra="forbid")


class CreatorSchema(BaseModel):
    name: str = Field(max_length=25)
    country: CountrySchema | None


if __name__ == "__main__":
    country = CountrySchema(**{"name": "China"})
    creator = CreatorSchema(**{"name": "Toyota", "country": None})
    print(creator.model_dump())
