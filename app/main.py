from fastapi import FastAPI
from app.routes import trade_routes

app = FastAPI()

app.include_router(trade_routes.router)

@app.get("/")
def root():
    return {"message": "senate trade scraper db"}