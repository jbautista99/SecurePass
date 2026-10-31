from datetime import datetime

login_history = []


def add_login_attempt(location, result):
    
    login_history.append({
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "location": location,
        "result": result
    })


def get_login_history():
    return login_history