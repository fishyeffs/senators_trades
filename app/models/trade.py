from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# read trade
# null non-optional fields should mean trade is rejected from db
class TradeRead(BaseModel):
    id: int
    politician_name : str
    party : str
    chamber : Optional[str] = None
    state : Optional[str] = None
    traded_issuer : str
    transaction_date : datetime
    transaction_type : str
    transaction_amount : str


class TradeCreate(BaseModel):
    id: int
    politician_name : str
    party : str
    chamber : Optional[str] = None
    state : Optional[str] = None
    traded_issuer : str
    transaction_date : datetime
    transaction_type : str
    transaction_amount : str