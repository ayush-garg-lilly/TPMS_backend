from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.api.crud.trials import create_trial, get_trials, get_trial_by_id, update_trial, delete_trial
from app.schemas.trial import TrialCreate, Trial, TrialUpdate
from app.api.crud.participant import create_participant, get_participants, get_participants_by_trial, update_participant, delete_participant
from app.schemas.participant import ParticipantCreate, Participant, ParticipantUpdate

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

@api_router.get("/trials/{trial_id}/participants", response_model= list[Participant])
def get_participants_for_trial(trial_id : int, db: Session = Depends(get_db)):
    trial= get_trial_by_id(db, trial_id)
    if not trial:
        raise HTTPException(status_code=404, detail="Trial not found")
    return get_participants_by_trial(db, trial_id)

@api_router.put("/trials/{trial_id}", response_model=Trial)
def update_trial_endpoint(
    trial_id: int,
    trial_data: TrialUpdate,
    db: Session = Depends(get_db)
):
    trial= update_trial(db, trial_id, trial_data)
    if not trial:
        raise HTTPException(status_code=404, detail="Trial not found")
    return trial

@api_router.put("/participants/{participant_id}", response_model=Participant)
def update_participant_endpoint(
    participant_id: int,
    participant_data: ParticipantUpdate,
    db: Session = Depends(get_db)
):
    participant= update_participant(db, participant_id, participant_data)
    if not participant:
        raise HTTPException(status_code=404, detail="Participant not found")
    return participant

@api_router.delete("/trials/{trial_id}")
def delete_trial_endpoint(trial_id: int, db: Session = Depends(get_db)):
    trial = delete_trial(db, trial_id)
    if not trial:
        raise HTTPException(status_code=404, detail="Trial not found")
    return {"detail": "Trial deleted"}

@api_router.delete("/participants/{participant_id}")
def delete_participant_endpoint(participant_id: int, db: Session = Depends(get_db)):
    participant = delete_participant(db, participant_id)
    if not participant:
        raise HTTPException(status_code=404, detail="Participant not found")
    return {"detail": "Participant deleted"}

@api_router.get("/trials/filter")
def list_trials_filtered(
    phase: str | None = None,
    name: str | None = None,
    description: str | None = None,
    search: str | None = None,
    limit: int = 100,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    filters = {
        "phase": phase,
        "name": name,
        "description": description
    }
    return get_trials(db, filters= filters, search= search, limit= limit, offset= offset)

@api_router.get("/participants/filter")
def list_participants_filtered(
    first_name: str | None = None,
    last_name: str | None = None,
    age: int | None = None,
    trial_id: int | None = None,
    search: str | None = None,
    limit: int = Query(100),
    offset: int = Query(0),
    db: Session = Depends(get_db)
):
    filters = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "trial_id": trial_id
    }

    return get_participants(db, filters=filters, search=search, limit=limit, offset=offset)