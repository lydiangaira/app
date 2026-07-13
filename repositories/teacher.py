from database import get_connection

def add_teacher(name, email, department, salary, id_number):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO teachers (name, email, department, salary, id_number) VALUES (?, ?, ?, ?, ?)",
            (name, email, department, salary, id_number),
        )
        connection.commit()

def get_teachers():
    with get_connection() as connection:
        return connection.execute("SELECT * FROM teachers").fetchall()
    
def update_teacher(teacher_id, name, email, department, salary, id_number):
    with get_connection() as connection:
        return connection.execute(
            "UPDATE teachers SET name=?, email=?, department=?, salary=?, id_number=? WHERE id=?",
            (name, email, department, salary, id_number, teacher_id)
        )

def delete_teacher(teacher_id):
    with get_connection() as connection:
        return connection.execute("DELETE FROM teachers WHERE id = ?", (teacher_id,))