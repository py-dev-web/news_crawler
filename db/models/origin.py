from sqlalchemy.orm import mapped_column
from sqlalchemy.types import String, Integer
from db.engine import Base


class Origin(Base):
    __tablename__ = 'origins'

    id      = mapped_column(Integer, primary_key=True, autoincrement=True)
    name    = mapped_column(String)
    symbol  = mapped_column(String)
    link    = mapped_column(String)

    def __repr__(self):
        return f"<Origin(id={self.id}, name={self.name})>"

