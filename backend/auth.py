import sqlite3
import bcrypt


def register_user(email, password):
    conn = sqlite3.connect("securepass.db")
    cursor = conn.cursor()

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            "INSERT INTO users (email, password_hash) VALUES (?, ?)",
            (
                email,
                password_hash.decode("utf-8")
            )
        )

        conn.commit()

        return {
            "message": "User registered successfully."
        }

    except sqlite3.IntegrityError:
        return {
            "error": "Email already exists."
        }

    finally:
        conn.close()


def login_user(email, password):
    conn = sqlite3.connect("securepass.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash FROM users WHERE email = ?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        return {
            "error": "User Not Found."
        }

    stored_hash = user[0]

    if bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8")
    ):
        return {
            "message": "Login successful."
        }

    return {
        "error": "Invalid password."
    }