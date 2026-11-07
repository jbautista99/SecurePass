# Imports
from fastapi import FastAPI
from pydantic import BaseModel
from password_checker import check_password_strength
from auth import register_user, login_user
from database import create_database
from geofencing import check_location
from login_history import get_login_history
from security_alerts import get_alert_history

# FastAPI app
app = FastAPI()

create_database()

# Request Models
class PasswordRequest(BaseModel):
    password: str


class UserRequest(BaseModel):
    email: str
    password: str
    location: str


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

    login_result = login_user(
        request.email,
        request.password
    )

    geofence_result = check_location(
        request.location
    )

    return {
        "authentication": login_result,
        "geofencing": geofence_result
    }

@app.post("/check-location")
def check_location_route(request: LocationRequest):
    return check_location(
        request.location
    )

@app.get("/login-history")
def login_history():
    return get_login_history()

@app.get("/security-alerts")
def security_alerts():
    return get_alert_history()