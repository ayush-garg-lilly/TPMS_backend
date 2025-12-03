from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.orm import relationship
from app.db.base import Base

class Trial(Base):
    __tablename__ = "trials"

    id= Column(Integer, primary_key= True, index= True)
    name= Column(String, nullable= False)
    phase= Column(String, nullable= False)
    description= Column(String, nullable= True)
    start_date= Column(Date, nullable= True)
    end_date= Column(Date, nullable= True)

    participants= relationship("Participant", 
                               back_populates= "trial",
                               cascade= "all, delete-orphan")