# Imports
from fastapi import FastAPI
from pydantic import BaseModel
from password_checker import check_password_strength
from auth import register_user, login_user
from database import create_database
from geofencing import check_location
from login_history import get_login_history

# FastAPI app
app = FastAPI()

create_database()

# Request Models
class PasswordRequest(BaseModel):
    password: str


class UserRequest(BaseModel):
    email: str
    password: str


class LocationRequest(BaseModel):
    location: str

# Routes
@app.get("/")
def home():
    return {"message": "Welcome to SecurePass!"}

@app.post("/check-password")
def analyze_password(request: PasswordRequest):
    return check_password_strength(request.password)

@app.post("/register")
def register(request: UserRequest):
    return register_user(
        request.email,
        request.password
    )

@app.post("/login")
def login(request: UserRequest):
    return login_user(
        request.email,
        request.password
    )

@app.post("/check-location")
def check_location_route(request: LocationRequest):
    return check_location(
        request.location
    )

@app.get("/login-history")
def login_history():
    return get_login_history()