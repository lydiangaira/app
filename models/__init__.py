from models import student, teacher, course

def create_tables():
    student.create_table()
    teacher.create_table()
    course.create_table()