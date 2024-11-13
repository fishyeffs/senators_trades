from pydantic import BaseModel

## pydantic api trade model
class Trade(BaseModel):
    politician_name: str
    party: str
    chamber: str
    state: str
    traded_issuer: str
    transaction_date: str
    transaction_type: str
    transaction_amount: str