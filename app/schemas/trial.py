#pydantic schema

from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Optional

class TrialBase(BaseModel):
    name: str = Field(min_length=1,max_length= 50)
    phase: str = Field(pattern=r"^(1|2|3|4)$")
    description: str | None = Field(None, max_length= 500)
    start_date: date | None = None
    end_date: date | None = None

    @validator("end_date")
    def end_after_start(cls, v, values):
        start= values.get("start_date")
        if start and v and v < start:
            raise ValueError("end_date must be after start_date")
        return v

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
        