from sqlalchemy import Column, String
from ...db.database import Base

class Work(Base):
    __tablename__ = "works"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    address = Column(String)
    neighborhood = Column(String)
    city = Column(String)
    state = Column(String)
    budget = Column(String)
    status = Column(String)
    image_url = Column(String)
    

