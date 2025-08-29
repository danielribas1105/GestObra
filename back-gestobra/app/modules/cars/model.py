from sqlalchemy import Column, String
from ...db.database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(String, primary_key=True, index=True)
    model = Column(String, index=True)
    plate = Column(String, unique=True, index=True)
    driver = Column(String)
    manufacturing = Column(String)
    km = Column(String)
    fuel = Column(String)
    strength = Column(String)
    capacity = Column(String)
    versatility = Column(String)
    status = Column(String)
    image_url = Column(String)

