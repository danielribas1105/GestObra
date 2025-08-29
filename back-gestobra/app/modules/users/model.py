from sqlalchemy import Column, String
from ...db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    cpf = Column(String)
    position = Column(String)
    profile = Column(String)
    status = Column(String)
    image_url = Column(String)
    password_hash = Column(String)

