from app.handlers.country import router as country_router
from app.handlers.creator import router as creator_router

from fastapi import APIRouter

main_router = APIRouter()

main_router.include_router(country_router)
main_router.include_router(creator_router)
