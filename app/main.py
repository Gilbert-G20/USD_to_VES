import datetime
from fastapi import FastAPI
from app.get_paralell import get_usd_ves_ratePL
from app.get_bcv import get_usd_ves_rateBCV
app = FastAPI()

@app.get("/api/rate-bcv")
def get_rateBCV():  
    data = get_usd_ves_rateBCV()  
    return {
        "currency": "USD-BCV",
        "to": "VES",
        "rate": data.get("rate", "N/A"),
        "updated_at": datetime.datetime.utcnow().isoformat()
    }

@app.get("/api/rate-parallel")
def get_ratePL():  
    data = get_usd_ves_ratePL()  
    return {
        "currency": "USD-Parallel",
        "to": "VES",
        "rate": data.get("rate", "N/A"),
        "updated_at": datetime.datetime.utcnow().isoformat()
    }