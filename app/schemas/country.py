from pydantic import BaseModel, ConfigDict, Field


class CountryAddSchema(BaseModel):
    name: str = Field(max_length=25)

    model_config = ConfigDict(extra="forbid")

class CountrySchema(CountryAddSchema):
    id: int
        
