from pydantic import BaseModel

class ParticipantBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    condition: str | None = None
    trial_id: int

class ParticipantCreate(ParticipantBase):
    pass

class Participant(ParticipantBase):
    id: int
    class Config:
        from_attributes = True

