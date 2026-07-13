from database import get_connection

def add_student(name, age, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO students (name, age, email, country, id_number) VALUES (?, ?, ?, ?, ?)",
            (name, age, email, country, id_number),
            )
        connection.commit()

def get_students():
    with get_connection() as connection:
        return connection.execute("SELECT * FROM students").fetchall()

def update_student(student_id, name, age, email, country, id_number):
    with get_connection() as connection:
        return connection.execute(
            "UPDATE students SET name=?, age=?, email=?, country=?, id_number=? WHERE id=?",
            (name, age, email, country, id_number, student_id)
        )
        

def delete_student(student_id):
    with get_connection() as connection:
        return connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
    