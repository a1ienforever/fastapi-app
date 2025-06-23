
from app.model import CountryModel
from app.services.base import BaseService


class CountryService(BaseService):
    model = CountryModel