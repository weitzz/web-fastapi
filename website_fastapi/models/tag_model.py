
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped,mapped_column,registry
from website_fastapi.core.database import Base

table_registry = registry()

@table_registry.mapped_as_dataclass
class TagModel(Base):
    __tablename__: str = 'tags'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tag: Mapped[str] = mapped_column(String(100))
    