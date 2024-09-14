from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import get_config

conf = get_config('database')
SQLALCHEMY_DATABASE_URL = f"postgresql://{conf['username']}:{conf['password']}@{conf['host']}/{conf['name']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
