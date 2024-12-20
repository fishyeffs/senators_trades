from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

## sqlalchemy db schema
## TODO normalise to two tables, politicians (unique = politician name) and trades (unique = trade ID) 
class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    politician_name = Column(String, index=True)
    party = Column(String)
    chamber = Column(String)
    state = Column(String)
    traded_issuer = Column(String)
    transaction_date = Column(DateTime)
    transaction_type = Column(String)
    transaction_amount = Column(String)