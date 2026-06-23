from database import create_table, add_student, get_students
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

create_table()



class Student(BaseModel):
    name: str
    age: int
    email: str
    country: str
    id_number: int

class Teacher(BaseModel):
    name: str
    email: str
    department: str
    salary: float
    id_number: int

class Course(BaseModel):
    title: str
    code: str
    credits: int
    department: str
    max_capacity: int
    status: str

@app.post("/students")
def register_student(student: Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student registered", "student": student}

@app.get("/students")
def list_students():
    students = get_students()
    return students

@app.put("/students/{student_id}")
def edit_student(student_id: int, student: Student):
    from database import update_student
    updated = update_student(student_id, student.name, student.age, student.email, student.country, student.id_number)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully", "student": student}

@app.delete("/students/{student_id}")
def remove_student(student_id: int):
    from database import delete_student
    deleted = delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}



@app.post("/teachers")
def register_teacher(teacher: Teacher):
    from database import add_teacher
    add_teacher(teacher.name, teacher.email, teacher.department, teacher.salary, teacher.id_number)
    return {"message": "Teacher registered", "teacher": teacher}

@app.get("/teachers")
def list_teachers():
    from database import get_teachers
    teachers = get_teachers()
    return teachers

@app.put("/teachers/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    from database import update_teacher
    updated = update_teacher(teacher_id, teacher.name, teacher.email, teacher.department, teacher.salary, teacher.id_number)
    if not updated:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"message": "Teacher updated successfully", "teacher": teacher}

@app.delete("/teachers/{teacher_id}")
def remove_teacher(teacher_id: int):
    from database import delete_teacher
    deleted = delete_teacher(teacher_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"message": "Teacher deleted successfully"}



@app.post("/courses")
def register_course(course: Course):
    from database import add_course
    add_course(course.title, course.code, course.credits, course.department, course.max_capacity, course.status)
    return {"message": "Course registered", "course": course}

@app.get("/courses")
def list_courses():
    from database import get_courses
    courses = get_courses()
    return courses

@app.put("/courses/{course_id}")
def edit_course(course_id: int, course: Course):
    from database import update_course
    updated = update_course(course_id, course.title, course.code, course.credits, course.department, course.max_capacity, course.status)
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course updated successfully", "course": course}

@app.delete("/courses/{course_id}")
def remove_course(course_id: int):
    from database import delete_course
    deleted = delete_course(course_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}
