
from fastapi import APIRouter

from app.database import SessionDep
from app.schemas.country import CountryAddSchema, CountrySchema
from app.schemas.pagination import PaginationDep
from app.services.country_service import CountryService

router = APIRouter(prefix="/countries", tags=["countries"])


@router.get("/")
async def list_countries(session: SessionDep, pagination: PaginationDep) -> list[CountrySchema]:
    return await CountryService.find_all(session, pagination)

@router.get("/{country_id}")
async def get_country(country_id: int, session: SessionDep) -> CountrySchema:
    return await CountryService.find_by_id(model_id=country_id , session=session)

@router.post("/")
async def add_country(country: CountryAddSchema, session: SessionDep) -> CountrySchema:
    new_country = await CountryService.create(data=country.model_dump(), session=session)

    return new_country