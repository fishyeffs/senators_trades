import json
from typing import List
from app.models.trade import Trade

def get_all_trades() -> List[Trade]:
    with open('politician_trades.json', 'r') as f:
        trades_data = json.load(f)
        return [Trade(**trade) for trade in trades_data]

def get_trade_by_id(trade_id: int) -> Trade:
    trades = get_all_trades()
    if 0 <= trade_id < len(trades):
        return trades[trade_id]
    return None