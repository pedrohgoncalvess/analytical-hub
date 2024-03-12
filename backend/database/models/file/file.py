from sqlalchemy import Column, Integer, String, Numeric, DateTime, Boolean, func
from sqlalchemy.orm import relationship
from database.models.base import Base
from database.models.file.schema import Schema


class File(Base):
    __tablename__ = 'file'
    __table_args__ = {'schema': 'file'}

    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    type = Column(String(10), nullable=False)
    size = Column(Numeric, nullable=False)
    nb_columns = Column(Integer, nullable=False)
    nb_rows = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    created_by = Column(Integer)
    status = Column(Boolean, nullable=False, default=True)
    file_schema_fk = relationship("Schema", backref="file.schema")
