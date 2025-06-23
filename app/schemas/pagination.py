from typing import Annotated

from pydantic import BaseModel, Field
from fastapi import Depends


class PaginationParams(BaseModel):
    limit: int = Field(5, ge=0, le=100, description="Кол-во элементов на странице")
    offset: int = Field(0, ge=0, description="Смещение для пагинации")


PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]

