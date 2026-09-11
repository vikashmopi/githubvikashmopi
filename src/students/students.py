# A simple dictionary representing our student database
STUDENTS_DB = {
    1: {"name": "vikash", "grade": "B"},
    2: {"name": "jithu", "grade": "A"}
}

def get_student(student_id):
    """
    Simulates a GET Student API.
    Returns the student details if found, or an error message if not.
    """
    if student_id in STUDENTS_DB:
        return {"status": 200, "data": STUDENTS_DB[student_id]}
    else:
        return {"status": 404, "error": "Student not found"}
