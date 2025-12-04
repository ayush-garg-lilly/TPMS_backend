from sqlalchemy.orm import Session
#from app.db.models import Trial
from app.db.models.trial import Trial as TrialModel
from app.schemas.trial import TrialCreate, TrialUpdate
from sqlalchemy import or_

def create_trial(db: Session, trial: TrialCreate):
    db_trial= TrialModel(**trial.dict())
    db.add(db_trial)
    db.commit()
    db.refresh(db_trial)
    return db_trial

def get_trials(db: Session, filters: dict = {}, search: str | None = None, limit: int = 100, offset: int = 0):
    query = db.query(TrialModel)

    for field, value in filters.items():
        if hasattr(TrialModel, field) and value is not None:
            query = query.filter(getattr(TrialModel, field) == value)

    if search:
        query = query.filter(
            or_(
                TrialModel.name.ilike(f"%{search}%"),
                TrialModel.description.ilike(f"%{search}%")
            )
        )

    return query.offset(offset).limit(limit).all()

def get_trial_by_id(db: Session, trial_id: int):
    return db.query(TrialModel).filter(TrialModel.id == trial_id).first()

def update_trial(db: Session, trial_id: int, trial_data: TrialUpdate):
    trial= db.query(TrialModel).filter(TrialModel.id == trial_id).first()
    if not trial:
        return None
    
    for key, value in trial_data.dict(exclude_unset=True).items():
        setattr(trial, key, value)
    db.commit()
    db.refresh(trial)
    return trial

def delete_trial(db: Session, trial_id: int):
    trial= db.query(TrialModel).filter(TrialModel.id == trial_id).first()
    if not trial:
        return None
    db.delete(trial)
    db.commit()
    return trial

