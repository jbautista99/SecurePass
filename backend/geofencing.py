# geofencing.py

from login_history import add_login_attempt

SOUTHWEST_REGION = [
    "Arizona",
    "California",
    "Colorado",
    "Nevada",
    "New Mexico",
    "Utah"
]

def check_location(location):

    location = location.strip().title()

    if location in SOUTHWEST_REGION:

        add_login_attempt(
            location,
            "Inside Geofence"
        )

        return {
            "inside_geofence": True,
            "zone": "Southwest Region",
            "message": "Location is inside the approved geofence.",
            "risk_level": "Low"
        }

    if location.isalpha():

        add_login_attempt(
            location,
            "Outside Geofence"
        )

        return {
            "inside_geofence": False,
            "zone": "Outside Region",
            "message": "Location is outside the approved geofence.",
            "risk_level": "Medium",
            "alert": "Security Alert - Unauthorized access attempt detected."
        }

    add_login_attempt(
        location,
        "Invalid Location"
    )

    return {
        "inside_geofence": False,
        "zone": "Invalid Location",
        "message": "Invalid location entered. Please provide a valid location.",
        "risk_level": "High",
        "alert": "Security Alert - Unauthorized access attempt detected."
    }