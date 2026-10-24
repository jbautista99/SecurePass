# geofencing.py

SOUTHWEST_REGION = [
    "Arizona",
    "California",
    "Colorado",
    "Nevada",
    "New Mexico",
    "Utah"
]

def check_location(location):

    location = location.strip()

    if location in SOUTHWEST_REGION:
        return {
            "inside_geofence": True,
            "zone": "Southwest Region",
            "message": "Location is inside the approved geofence."
        }

    if location.isalpha():
        return {
            "inside_geofence": False,
            "zone": "Outside Region",
            "message": "Location is outside the approved geofence."
        }

    return {
        "inside_geofence": False,
        "zone": "Invalid Location",
        "message": "Invalid location entered. Please provide a valid location."
    }