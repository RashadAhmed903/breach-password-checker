from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from hibp import count_password_breaches
from scorer import estimate_crack_seconds, estimate_entropy_bits, rate_password

app = FastAPI()


class PasswordCheckRequest(BaseModel):
    password: str


@app.post("/check-password")
def check_password(request: PasswordCheckRequest):
    breach_count = count_password_breaches(request.password)
    is_breached = breach_count > 0
    entropy_bits = estimate_entropy_bits(request.password)

    if is_breached:
        rating = "very weak"
        crack_seconds = 0.0
    else:
        rating = rate_password(entropy_bits)
        crack_seconds = estimate_crack_seconds(entropy_bits)

    return {
        "breached": is_breached,
        "breach_count": breach_count,
        "entropy_bits": round(entropy_bits, 1),
        "crack_seconds": crack_seconds,
        "rating": rating,
    }


app.mount("/", StaticFiles(directory="static", html=True), name="static")