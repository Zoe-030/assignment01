
# app/models.py
from sqlalchemy import Column, Integer, DateTime, func
from app.db import Base

# ORM model for the health_checks table
class HealthCheck(Base):
    __tablename__ = "health_checks"

    # Primary key, auto-incremented
    check_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Timestamp of the health check, defaults to current UTC time
    check_datetime = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
