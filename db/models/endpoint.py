from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime, String, Integer
from sqlalchemy import func
from db.engine import Base


class Endpoint(Base):
    __tablename__ = 'endpoints'

    id          = mapped_column(Integer, primary_key=True, autoincrement=True)
    origin_id   = mapped_column(Integer)
    category    = mapped_column(String)
    endpoint    = mapped_column(String)
    updated_at  = mapped_column(DateTime,default=None,server_default=func.now(),
                                onupdate=func.now(),nullable=True)

    def __repr__(self):
        return f"<Origin(id={self.id}, name={self.endpoint})>"

