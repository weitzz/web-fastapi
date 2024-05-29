from typing import List


from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from website_fastapi.core.database import Base
from website_fastapi.models.tag_model import TagModel




tags_author = Table(
    'tags_author',
    Base.metadata,
    Column('id_author', Integer, ForeignKey('authors.id')),
    Column('id_tag', Integer, ForeignKey('tags.id'))
)


class AuthorModel(Base):
    __tablename__: str = 'authors'

    id: int = Column(Integer,primary_key=True, autoincrement=True)
    name:str = Column(String(100))
    avatar: str  = Column(String(100))  # 40x40

    # Um autor pode ter várias tags
    tags: List[TagModel] =relationship('TagModel', back_populates='tags_author', lazy='joined')
    __allow_unmapped__ = True