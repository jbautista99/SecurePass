from datetime import datetime

security_alerts = []


def add_alert(location, risk_level, message):

    security_alerts.append({
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "location": location,
        "risk_level": risk_level,
        "message": message
    })


def get_alert_history():
        
    return security_alerts