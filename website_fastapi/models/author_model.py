from typing import List


from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped,mapped_column,registry,relationship
from website_fastapi.core.database import Base
from website_fastapi.models.tag_model import TagModel

table_registry = registry()



tags_author = Table(
    'tags_author',
    Base.metadata,
    mapped_column('id_author', Integer, ForeignKey('authors.id')),
    mapped_column('id_tag', Integer, ForeignKey('tags.id'))
)

@table_registry.mapped_as_dataclass
class AuthorModel(Base):
    __tablename__: str = 'authors'

    id: Mapped[int] = mapped_column(Column,primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    avatar: Mapped[str]  = mapped_column(String(100))  # 40x40

    # Um autor pode ter várias tags
    tags: Mapped[List[TagModel]] =relationship('TagModel', secondary=tags_author, backref='taga', lazy='joined')
    