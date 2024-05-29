
from sqlalchemy import Column, Integer, String

from website_fastapi.core.database import Base


class TagModel(Base):
    __tablename__: str = 'tags'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    tag: str = Column(String(100))
    