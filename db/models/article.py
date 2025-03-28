from sqlalchemy.orm import mapped_column
from sqlalchemy.types import String, Integer, LargeBinary, DateTime
from db.engine import Base


class Article(Base):
    __tablename__ = 'articles'

    id              = mapped_column(Integer, primary_key=True, autoincrement=True)
    title           = mapped_column(String)
    endpoint_id     = mapped_column(Integer)
    identifier      = mapped_column(String)
    body            = mapped_column(LargeBinary)
    link            = mapped_column(String)
    author          = mapped_column(String, default="")
    published_at    = mapped_column(DateTime)


    def __repr__(self):
        return f"<Origin(id={self.id}, name={self.title})>"

