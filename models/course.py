from database import get_connection

def create_table():
    with get_connection() as connection:
        connection.execute("""
                CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                code TEXT NOT NULL,
                credits INTEGER NOT NULL,
                department TEXT NOT NULL,
                max_capacity INTEGER NOT NULL,
                status TEXT NOT NULL
                )
        """)