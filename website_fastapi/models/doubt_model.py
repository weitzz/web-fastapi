from website_fastapi.models.area_model import AreaModel
from sqlalchemy import  ForeignKey, Integer, String,Column

from website_fastapi.core.database import Base
from sqlalchemy.orm import relationship

class DoubtModel(Base):
    __tablename__: str = 'doubts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_area = Column(Integer, ForeignKey('areas.id'))
    area = relationship('AreaModel', back_populates='doubts')

    title = Column(String(200), nullable=False)
    answer = Column(String(400), nullable=False)
