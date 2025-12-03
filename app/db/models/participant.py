from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship

class Participant(Base):
    __tablename__ = "participants"

    id= Column(Integer, primary_key= True, index= True)
    first_name= Column(String, nullable= False)
    last_name= Column(String, nullable= False)
    age= Column(Integer, nullable= False)
    condition = Column(String, nullable= True)

    trial_id= Column(Integer, ForeignKey("trials.id"))
    trial= relationship("Trial", back_populates= "participants")