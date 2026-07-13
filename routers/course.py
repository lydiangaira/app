from fastapi import APIRouter
from schemas.course import Course
from repositories.course import (
    add_course,
    get_courses,
    update_course,
    delete_course,
) 

router = APIRouter(prefix="/courses", tags=["courses"])

@router.post("")
def register_course(course: Course):
    add_course(course.title, course.code, course.credits, course.department, course.max_capacity, course.status)
    return {"message": "Course registered", "course": course}

@router.get("/courses")
def list_courses():
    courses = get_courses()
    return courses

@router.put("/{course_id}")
def edit_course(course_id: int, course: Course):
    update_course(course_id, course.title, course.code, course.credits, course.department, course.max_capacity, course.status)
    return {"message": "Course updated successfully", "course": course}

@router.delete("/{course_id}")
def remove_course(course_id: int):
    delete_course(course_id)
    return {"message": "Course deleted successfully"}