from datetime import datetime
from typing import List
from models.author_model import AuthorModel
from models.tag_model import TagModel
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
)

from website_fastapi.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, registry,relationship

table_registry = registry()


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
    Column('id_comment', Integer, ForeignKey('comments_.id'))
)

@table_registry.mapped_as_dataclass
class PostModel(Base):

    __tablename__: str = 'posts'

    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    data: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, index=True)

    tags: List[TagModel] = relationship('TagModel', secondary=tags_post, backref='tagp', lazy='joined')

    image: Mapped[str] = mapped_column(String(100))  # 900x400
    text: Mapped[str] = mapped_column(String(1000))

    # Um Post pode ter vários comentários (Não importamos e usamos ComentarioModel como tipo de dados aqui pois causa erro de import circular com a tabela ComentarioModel)
    comments: List[object] = relationship('CommentsModel', secondary=comments_post, backref='comentario', lazy='joined')

    id_author: Mapped[int] = mapped_column(Integer, ForeignKey('authors.id'))
    author: Mapped[AuthorModel] = relationship('AuthorModel', lazy='joined')
    
