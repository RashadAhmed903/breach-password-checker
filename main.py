from fastapi import FastAPI
from pydantic import BaseModel

from hibp import count_password_breaches
app = FastAPI()
class PasswordCheckRequest(BaseModel):
    password: str

@app.get("/")
def read_root():
    return {"Massage" : "Hello from the breach and password health checker!"}

@app.post("/check-password")
def check_password(request: PasswordCheckRequest):
    breach_count = count_password_breaches(request.password)
    return {
        "breached": breach_count > 0,
        "breach_count": breach_count,
    }