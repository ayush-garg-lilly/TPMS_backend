#pydantic schema

from pydantic import BaseModel
from datetime import date
from typing import Optional

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

class TrialUpdate(BaseModel):
    name: Optional[str] = None
    phase: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    class Config:
        from_attributes = True
        