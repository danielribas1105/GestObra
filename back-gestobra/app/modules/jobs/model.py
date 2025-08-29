from sqlalchemy import Column, String
from ...db.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True)
    date = Column(String)
    plate_id = Column(String, unique=True, index=True)
    driver_id = Column(String)
    m3 = Column(String)
    origin = Column(String)
    destination = Column(String)
    status = Column(String)
    

