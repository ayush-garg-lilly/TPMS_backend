from pydantic import BaseModel
from typing import Optional

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

class ParticipantUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    condition: Optional[str] = None
    trial_id: Optional[int] = None

    class Config:
        from_attributes = True