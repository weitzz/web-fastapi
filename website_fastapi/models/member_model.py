
from sqlalchemy import  Integer, String,Column

from website_fastapi.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, registry

# table_registry = registry()


# @table_registry.mapped_as_dataclass
class MemberModel(Base):
    __tablename__: str = 'members'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100))
    role: str = Column(String(100))
    avatar: str = Column(String(100))
