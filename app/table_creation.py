from app.db.session import engine
from app.db.base import Base
from app.db.models import Trial, Participant  # Import all models here

Base.metadata.create_all(bind= engine)
print("Database tables created successfully.")