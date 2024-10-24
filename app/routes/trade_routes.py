from typing import List
from fastapi import APIRouter, HTTPException
from app.services.trade_service import get_all_trades, get_trade_by_id
from app.models.trade import Trade

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