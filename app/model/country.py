from sqlalchemy.orm import Mapped, mapped_column

from app.model.base import Base


class CountryModel(Base):
    __tablename__ = 'countries'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

