from sqlalchemy.orm import Session
from app.db.models import Trial
from app.schemas.trial import TrialCreate

def create_trial(db: Session, trial: TrialCreate):
    db_trial= Trial(**trial.dict())
    db.add(db_trial)
    db.commit()
    db.refresh(db_trial)
    return db_trial

def get_trials(db: Session):
    return db.query(Trial).all()