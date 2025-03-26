from typing import List
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import TEXT, String, Integer, LargeBinary, DateTime
from db.engine import Base


class News(Base):
    __tablename__ = 'news'

    id          = mapped_column(Integer, primary_key=True, autoincrement=True)
    title       = mapped_column(String)
    endpoint_id = mapped_column(Integer)
    identifier  = mapped_column(String)
    body        = mapped_column(LargeBinary)
    link        = mapped_column(String)
    author      = mapped_column(String, default="")
    published_at  = mapped_column(DateTime,default=None, server_default=func.now(), nullable=True)


    def __repr__(self):
        return f"<Origin(id={self.id}, name={self.title})>"

