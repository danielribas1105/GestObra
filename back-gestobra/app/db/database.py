from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

""" sqlite:///./db.sqlite3 """

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/gestobra"

""" engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) """
# No Postgres não precisa de connect_args
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
