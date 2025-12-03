from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.api.crud.trials import create_trial, get_trials
from app.schemas.trial import TrialCreate, Trial
from app.api.crud.participant import create_participant, get_participants
from app.schemas.participant import ParticipantCreate, Participant
from app.db.models.trial import Trial as TrialModel

api_router= APIRouter()

@api_router.get("/health")
def health_check():
    return {"status": "healthy"}

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@api_router.post("/trials", response_model=Trial)
def create_trial_endpoint(trial: TrialCreate, db: Session = Depends(get_db)):
    return create_trial(db, trial)

@api_router.get("/trials", response_model= list[Trial])
def get_trials_endpoint(db: Session = Depends(get_db)):
    return get_trials(db)

@api_router.post("/participants", response_model=Participant)
def create_participant_endpoint(participant: ParticipantCreate, db: Session = Depends(get_db)):
    return create_participant(db, participant)

@api_router.get("/participants", response_model= list[Participant])
def get_participants_endpoint(db: Session = Depends(get_db)):
    return get_participants(db)

@api_router.get("/trials/{trial_id}", response_model=Trial)
def get_trial_by_id(trial_id: int, db: Session = Depends(get_db)):
    trial= db.query(TrialModel).filter(TrialModel.id == trial_id).first()
    return trial