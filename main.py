
from fastapi import FastAPI

app = FastAPI(
    title="Monu Demo API",
    description="Synthetic test data API",
    version="1.0"
)

demo_records = [
    {
        "username": "Demo User 1",
        "mobile_number": "9999900001",
        "email": "demo1@example.com",
        "user_id": "DEMO001",
        "city": "Delhi",
        "state": "Delhi"
    },
    {
        "username": "Demo User 2",
        "mobile_number": "9999900002",
        "email": "demo2@example.com",
        "user_id": "DEMO002",
        "city": "Rohtak",
        "state": "Haryana"
    }
]

@app.get("/")
def home():
    return {"message": "Monu Demo API is running"}

@app.get("/api/health")
def health():
    return {"status": "online"}

@app.get("/api/demo/{user_id}")
def get_demo(user_id: str):
    for user in demo_records:
        if user["user_id"] == user_id:
            return user

    return {"error": "Demo record not found"}
  
