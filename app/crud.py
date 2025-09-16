
from sqlalchemy.orm import Session
from app.models import HealthCheck

def create_health_check(db: Session):
    record = HealthCheck()
    db.add(record)
    db.commit()
    return record
