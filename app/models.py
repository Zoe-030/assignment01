# app/models.py
from sqlalchemy import Column, Integer, DateTime, func
from app.db import Base


class HealthRecord(Base):
    __tablename__ = "health_checks"  # this is the actual table name inside Postgres

    # This is the unique ID for each row 
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # This column saves the exact time 
   
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
