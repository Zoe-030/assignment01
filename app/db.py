
# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# Create database engine (connection to PostgreSQL)
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,      # Print SQL statements for debugging
    future=True     # Use SQLAlchemy 2.0 style API
)

# Session factory: creates a new database session for each request
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

# Base class for ORM models (all models will inherit from this)
Base = declarative_base()

# Dependency for getting a database session
# Ensures each request has its own session and closes it afterwards
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
