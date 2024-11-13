import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.trade import Base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRADES_FILE_PATH = os.path.join(BASE_DIR, 'trades.json')
# maybe want to go with postgresql not sure yet
SQLALCHEMY_DATABASE_URL = "sqlite:///./db/trades.db"

# the rest of this was made using chatgpt
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()