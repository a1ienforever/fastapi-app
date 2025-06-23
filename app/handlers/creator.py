
from fastapi import APIRouter

from app.schemas.creator import CreatorSchema

router = APIRouter(prefix="/creators", tags=["creators"])

creators = []

@router.post("/")
async def add_creator(creator: CreatorSchema):
    creators.append(creator)
    return {'success': True, 'creators': creators}

@router.get("/")
async def list_creators() -> list[CreatorSchema]:
    return creators