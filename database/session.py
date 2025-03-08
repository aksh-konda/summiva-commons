from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pymongo import MongoClient
from config.settings import settings

# PostgreSQL Connection
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB Connection
mongo_client = MongoClient(settings.MONGODB_URI)
mongo_db = mongo_client["summiva"]
