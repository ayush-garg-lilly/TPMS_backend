from sqlalchemy.orm import Session
from app.db.models.participant import Participant as ParticipantModel
from app.schemas.participant import ParticipantCreate, ParticipantUpdate
from sqlalchemy import or_

def create_participant(db: Session, participant: ParticipantCreate):
    db_participant= ParticipantModel(**participant.dict())
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

def get_participants(db: Session, filters: dict = {}, search: str | None = None, limit: int = 100, offset: int = 0):
    query = db.query(ParticipantModel)

    for field, value in filters.items():
        if hasattr(ParticipantModel, field) and value is not None:
            query = query.filter(getattr(ParticipantModel, field) == value) 

    if search:
        query = query.filter(
            or_(
                ParticipantModel.first_name.ilike(f"%{search}%"),
                ParticipantModel.last_name.ilike(f"%{search}%")
            )
        )

    return query.offset(offset).limit(limit).all()

def get_participants_by_trial(db: Session, trial_id: int):
    return db.query(ParticipantModel).filter(ParticipantModel.trial_id == trial_id).all()

def update_participant(db: Session, participant_id: int, participant_data: ParticipantUpdate):
    db_participant= db.query(ParticipantModel).filter(ParticipantModel.id == participant_id).first()
    if not db_participant:
        return None
    update_data= participant_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_participant, key, value)
    db.commit()
    db.refresh(db_participant)
    return db_participant

def delete_participant(db: Session, participant_id: int):
    participant= db.query(ParticipantModel).filter(ParticipantModel.id == participant_id).first()
    if not participant:
        return None
    db.delete(participant)
    db.commit()
    return participant