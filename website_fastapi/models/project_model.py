from datetime import datetime


from sqlalchemy import Column, DateTime, Integer, String

from website_fastapi.core.database import Base



class ProjectModel(Base):
    __tablename__: str = 'projects'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    data: datetime = Column(DateTime, default=datetime.now, index=True)
    title: str = Column(String(100))
    description_inital: str = Column(String(300))
    image1: str = Column(String(100))  # 1300x700
    image2: str = Column(String(100))  # 600x400
    image3: str = Column(String(100))  # 600x400
    description_finish: str = Column(String(300))
    link: str = Column(String(200))
