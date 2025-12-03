from sqlalchemy.orm import Session
from app.db.models.participant import Participant as ParticipantModel
from app.schemas.participant import ParticipantCreate

def create_participant(db: Session, participant: ParticipantCreate):
    db_participant= ParticipantModel(**participant.dict())
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

def get_participants(db: Session):
    return db.query(ParticipantModel).all()