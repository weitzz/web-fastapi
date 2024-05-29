from models.area_model import AreaModel
from sqlalchemy import  ForeignKey, Integer, String

from website_fastapi.core.database import Base
from sqlalchemy.orm import Mapped,mapped_column,registry,relationship
table_registry = registry()


@table_registry.mapped_as_dataclass
class DoubtModel(Base):
    __tablename__: str = 'doubts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    id_area: Mapped[int] = mapped_column(Integer, ForeignKey('areas.id'))
    area: Mapped[AreaModel] =relationship('AreaModel', lazy='joined')

    title: Mapped[str] = mapped_column(String(200))
    answer: Mapped[str] = mapped_column(String(400))
