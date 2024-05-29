from datetime import datetime
from typing import List

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
)

from website_fastapi.core.database import Base
from sqlalchemy.orm import relationship

from website_fastapi.models.author_model import AuthorModel
from website_fastapi.models.tag_model import TagModel



tags_post = Table(
    'tags_post',
    Base.metadata,
    Column('id_post', Integer, ForeignKey('posts.id')),
    Column('id_tag', Integer, ForeignKey('tags.id'))
)


comments_post = Table(
    'comments_post',
    Base.metadata,
    Column('id_post', Integer, ForeignKey('posts.id')),
    Column('id_comment', Integer, ForeignKey('comments.id'))
)


class PostModel(Base):

    __tablename__: str = 'posts'

    id:int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(200))
    data: datetime = Column(DateTime, default=datetime.now, index=True)
    image: str = Column(String(100))  # 900x400
    text: str = Column(String(1000))

    tags: List[TagModel] = relationship('TagModel', secondary=tags_post, backref='posts', lazy='joined')

    # Um Post pode ter vários comentários (Não importamos e usamos ComentarioModel como tipo de dados aqui pois causa erro de import circular com a tabela ComentarioModel)
    comments: List[object] = relationship('CommentsModel', back_populates='comments_post', lazy='joined')

    id_author: int = Column(Integer, ForeignKey('authors.id'))
    author: AuthorModel = relationship('AuthorModel', back_populates='posts',lazy='joined')
    
    __allow_unmapped__ = True