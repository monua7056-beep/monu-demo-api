
from fastapi import FastAPI, Query

app = FastAPI(title="Monu Cyber Lab")

demo_data = {
    "0000000001": {
        "username": "Demo User One",
        "mobile_number": "0000000001",
        "email": "demo1@example.com",
        "user_id": "DEMO001",
        "city": "Delhi"
    },
    "0000000002": {
        "username": "Demo User Two",
        "mobile_number": "0000000002",
        "email": "demo2@example.com",
        "user_id": "DEMO002",
        "city": "Rohtak"
    }
}

@app.get("/api/demo")
def search_demo(number: str = Query(...)):
    if not number.isdigit() or len(number) != 10:
        return {"message": "Invalid demo number"}

    result = demo_data.get(number)

    if result:
        return result

    return {"message": "No demo record found"}
    
