from datetime import datetime

from sqlalchemy import  DateTime, ForeignKey, Integer, String,Column
from sqlalchemy.orm import relationship
from website_fastapi.core.database import Base
from website_fastapi.models.post_model import PostModel

class CommentModel(Base):
    __tablename__: str = 'comments'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    data: datetime = Column(DateTime, default=datetime.now, index=True)
    author: str = Column(String(200))
    text: str = Column(String(400))

    id_post: int = Column(Integer, ForeignKey('posts.id'))
    post: PostModel = relationship('PostModel', back_populates='comments')

    __allow_unmapped__ = True