
from sqlalchemy import Column, Integer, String

from website_fastapi.core.database import Base
from sqlalchemy.orm import relationship



class AreaModel(Base):
    """Dúvidas respondidas no FAQ são categorizadas em áreas"""
    __tablename__: str = 'areas'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    area: str = Column(String(100))
    doubts = relationship('DoubtModel', back_populates='area')