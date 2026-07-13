from database import get_connection

def create_table():
    with get_connection() as connection:
        connection.execute("""
                CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL,
                id_number INTEGER NOT NULL
                )
        """)