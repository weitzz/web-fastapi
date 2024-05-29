
from sqlalchemy import Column, Integer, String

from website_fastapi.core.database import Base
from sqlalchemy.orm import Mapped,mapped_column,registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class AreaModel(Base):
    """Dúvidas respondidas no FAQ são categorizadas em áreas"""
    __tablename__: str = 'areas'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    area: Mapped[str] = mapped_column(String(100))
