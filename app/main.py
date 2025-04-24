import datetime
from fastapi import FastAPI
from app.get_paralell import get_usd_ves_rateBCV
from app.get_bcv import get_usd_ves_ratePL
app = FastAPI()

@app.get("/api/rate")
def get_rateBCV():  
    data = get_usd_ves_rateBCV()  
    return {
        "currency": "USD-BCV",
        "to": "VES",
        "rate": data.get("rate", "N/A"),
        "updated_at": datetime.utcnow().isoformat()
    }

def get_ratePL():  
    data = get_usd_ves_ratePL()  
    return {
        "currency": "USD-Parallel",
        "to": "VES",
        "rate": data.get("rate", "N/A"),
        "updated_at": datetime.utcnow().isoformat()
    }