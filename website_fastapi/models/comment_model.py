from datetime import datetime

from models.post_model import PostModel
from sqlalchemy import  DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped,mapped_column,registry,relationship
from website_fastapi.core.database import Base
table_registry = registry()


@table_registry.mapped_as_dataclass
class CommentModel(Base):
    __tablename__: str = 'comments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    data: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, index=True)

    id_post: Mapped[int] = mapped_column(Integer, ForeignKey('posts.id'))
    post: Mapped[PostModel] = relationship('PostModel', lazy='joined')

    author: Mapped[str] = mapped_column(String(200))
    text: Mapped[str] = mapped_column(String(400))
