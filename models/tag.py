from sqlalchemy import Column, Integer, String, ForeignKey
from common_lib.database.session import Base

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
