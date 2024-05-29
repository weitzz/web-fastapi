
from sqlalchemy import  Integer, String,Column

from website_fastapi.core.database import Base



class MemberModel(Base):
    __tablename__: str = 'members'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100))
    role: str = Column(String(100))
    avatar: str = Column(String(100))
