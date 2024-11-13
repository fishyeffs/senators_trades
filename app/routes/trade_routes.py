from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.services.trade_service import get_all_trades, get_trade_by_id
from app.models.trade import Trade
from app.schemas.trade import Trade as TradeCreate
from app.config import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/trades", response_model=List[Trade])
def get_trades():
    trades = get_all_trades()
    return trades

@router.get("/trades/{trade_id}", response_model=Trade)
def get_trade(trade_id: int):
    trade = get_trade_by_id(trade_id)
    if trade:
        return trade
    raise HTTPException(status_code=404)

## TODO auth
@router.post("/trades/", response_model=TradeCreate)
def create_trade(trade: TradeCreate, db: Session = Depends(get_db)):
    db_trade = Trade(
        politician_name=trade.politician_name,
        party=trade.party,
        chamber=trade.chamber,
        state=trade.state,
        traded_issuer=trade.traded_issuer,
        transaction_date=trade.transaction_date,
        transaction_type=trade.transaction_type,
        transaction_amount=trade.transaction_amount
    )
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade