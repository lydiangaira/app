from fastapi import APIRouter
from schemas.student import Student
from repositories.student import (
    add_student,
    get_students,
    update_student,
    delete_student,
) 

router = APIRouter(prefix="/students", tags=["students"])

@router.post("") #blank since we already have the prefix
def register_student(student: Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student registered successfully", "student": student}

@router.get("")
def list_students():
    return get_students()

@router.put("/{student_id}")
def edit_student(student: Student):
    update_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student updated successfully", "student": student}

@router.delete("/{student_id}")
def remove_student(student_id: int):
    delete_student(student_id)
    return {"message": "Student deleted successfully"}
