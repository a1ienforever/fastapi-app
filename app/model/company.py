from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.model import Base


class Company(Base):
    __tablename__ = 'companies'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.id'))