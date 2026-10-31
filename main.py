
import json
from pathlib import Path
from fastapi import FastAPI, Query

app = FastAPI(title="Monu Cyber Lab")

DB_FILE = Path(__file__).parent / "demo_data.json"

def load_database():
    with open(DB_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

@app.get("/")
def home():
    return {
        "project": "Monu Cyber Lab",
        "owner": "Monu Chaudhary",
        "status": "online"
    }

@app.get("/api/search")
def search_number(number: str = Query(...)):
    if not number.isdigit() or len(number) != 10:
        return {"message": "Invalid demo number"}

    records = load_database()

    for record in records:
        if record.get("mobile_number") == number:
            return {
                "status": "found",
                "data": record
            }

    return {
        "status": "not_found",
        "message": "No demo record found"
    }
    
