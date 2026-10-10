# geofencing.py

APPROVED_LOCATIONS = [
    "California"
]


def check_location(location):
    if location in APPROVED_LOCATIONS:
        return {
            "status": "approved",
            "message": "Login location approved."
        }

    return {
        "status": "flagged",
        "message": "Unrecognized login location detected."
    }