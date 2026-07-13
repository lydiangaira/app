from database import get_connection

def add_course(title, code, credits, department, max_capacity, status):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO courses (title, code, credits, department, max_capacity, status) VALUES (?, ?, ?, ?, ?, ?)",
            (title, code, credits, department, max_capacity, status),
            )
        connection.commit()

def get_courses():
    with get_connection() as connection:
        return connection.execute("SELECT * FROM courses").fetchall()
        

def update_course(course_id, title, code, credits, department, max_capacity, status):
    with get_connection() as connection:
        return connection.execute(
            "UPDATE courses SET title=?, code=?, credits=?, department=?, max_capacity=?, status=?, WHERE id=?",
            (title, code, credits, department, max_capacity, course_id, status)
        )
        

def delete_course(course_id):
    with get_connection() as connection:
        return connection.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        