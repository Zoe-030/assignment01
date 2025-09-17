
from sqlalchemy import Column, Integer, DateTime, func, Index
from app.db import Base


class HealthCheck(Base):
    __tablename__ = "health_checks"  

   
    check_id = Column(Integer, primary_key=True, autoincrement=True)

   
    check_datetime = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    def __repr__(self):
        return f"<HealthCheck(check_id={self.check_id}, check_datetime={self.check_datetime})>"



Index("idx_check_datetime", HealthCheck.check_datetime)
