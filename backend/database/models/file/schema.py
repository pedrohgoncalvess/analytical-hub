from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, ForeignKey, Computed
from sqlalchemy.orm import relationship
from database.models.base import Base


class Schema(Base):
    __tablename__ = 'schema'
    __table_args__ = {'schema': 'file'}

    id = Column(Integer, primary_key=True)
    id_table = Column(Integer, ForeignKey('file.file.id'), nullable=False)
    column_name = Column(String(50), nullable=False)
    column_type = Column(String(20), nullable=False)
    null = Column(Boolean, nullable=False)
    default = Column(String(20), nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=True)
    edited = Column(Boolean, nullable=False, default=False)
    compost_id = Column(String(100), Computed("generate_compost_id(id_pessoa, etapa)"), nullable=False, unique=True)
    schema_file_fk = relationship(
        "File",
        back_populates="file_schema_fk",
        primaryjoin="Schema.id_table == File.id",
        foreign_keys=[id_table]
    )
