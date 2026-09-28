from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Massage" : "Hello from the breach and password health checker!"}