from sqlalchemy import Column, String
from ...db.database import Base

class Statement(Base):
    __tablename__ = "statements"

    id = Column(String, primary_key=True, index=True)
    date = Column(String)
    manifest = Column(String, unique=True, index=True)
    status = Column(String)
    

