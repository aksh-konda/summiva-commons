from sqlalchemy import Column, Integer, String, Text
from common_lib.database.session import Base

class SearchIndex(Base):
    __tablename__ = "search_index"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, nullable=False)
    keyword_index = Column(Text, nullable=False)  # Used by Elasticsearch
    vector_index = Column(String, nullable=False)  # Used by FAISS
