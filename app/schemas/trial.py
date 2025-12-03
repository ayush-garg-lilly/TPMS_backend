#pydantic schema

from pydantic import BaseModel
from datetime import date

class TrialBase(BaseModel):
    name: str
    phase: str
    description: str | None = None
    start_date: date | None = None
    end_date: date | None = None

class TrialCreate(TrialBase):
    pass 

class Trial(TrialBase):
    id: int
    class Config:
        from_attributes = True
        