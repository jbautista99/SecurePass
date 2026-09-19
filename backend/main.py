from fastapi import FastAPI
from pydantic import BaseModel
from password_checker import check_password_strength

app = FastAPI()


class PasswordRequest(BaseModel):
    password: str


@app.get("/")
def home():
    return {"message": "Welcome to SecurePass!"}


@app.post("/check-password")
def analyze_password(request: PasswordRequest):
    return check_password_strength(request.password)