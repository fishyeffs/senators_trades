from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    politician_name = Column(String, index=True)
    party = Column(String)
    chamber = Column(String)
    state = Column(String)
    traded_issuer = Column(String)
    transaction_date = Column(String)
    transaction_type = Column(String)
    transaction_amount = Column(String)