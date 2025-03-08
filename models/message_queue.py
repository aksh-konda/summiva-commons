from sqlalchemy import Column, Integer, String, Text, Boolean
from common_lib.database.session import Base

class MessageQueue(Base):
    __tablename__ = "message_queue"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, nullable=False)
    status = Column(String, default="pending")  # 'pending', 'processing', 'completed', 'failed'
    payload = Column(Text, nullable=False)  # Stores JSON data
    processed = Column(Boolean, default=False)
