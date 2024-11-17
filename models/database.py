from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables
DATABASE_URL = os.getenv("POSTGRESQL_DATABASE_URL")

# Create the database engine
engine = create_engine(DATABASE_URL)  # Synchronous connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model for storing PDF metadata
class PDFMetadata(Base):
    __tablename__ = "pdf_metadata"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content = Column(Text)

# Create tables in PostgreSQL database (do this only once)
Base.metadata.create_all(bind=engine)
