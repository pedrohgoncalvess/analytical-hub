from sqlalchemy import Column, Integer, String, Numeric, DateTime
from database.models.base import Base


class File(Base):
    __tablename__ = 'file'
    __table_args__ = {'schema': 'file'}

    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    type = Column(String(10), nullable=False)
    size = Column(Numeric, nullable=False)
    columns = Column(Integer, nullable=False)
    rows = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(Integer)
