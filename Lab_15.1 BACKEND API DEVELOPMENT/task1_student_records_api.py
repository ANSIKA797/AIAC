"""Student Records RESTful API using FastAPI and in-memory storage."""
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title="Student Records API")
students_db: dict[int, dict] = {}


class Student(BaseModel):
    name: str
    branch: str
    gpa: float


@app.get("/students")
def list_students():
    """Return all stored student records."""
    return {"students": list(students_db.values())}


@app.post("/students", status_code=201)
def add_student(student_id: int, student: Student):
    """Create a new student record if ID does not already exist."""
    if student_id in students_db:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    record = {"id": student_id, **student.dict()}
    students_db[student_id] = record
    return record


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    """Update an existing student record by ID."""
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    students_db[student_id] = {"id": student_id, **student.dict()}
    return students_db[student_id]


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    """Delete a student record by ID."""
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    removed = students_db.pop(student_id)
    return {"deleted": removed}


if __name__ == "__main__":
    client = TestClient(app)
    r1 = client.post("/students?student_id=101", json={"name": "Ansika", "branch": "CSE", "gpa": 9.2})
    assert r1.status_code == 201 and r1.json()["name"] == "Ansika"
    r2 = client.get("/students")
    assert r2.status_code == 200 and len(r2.json()["students"]) == 1
    r3 = client.put("/students/101", json={"name": "Ansika", "branch": "AI&ML", "gpa": 9.4})
    assert r3.status_code == 200 and r3.json()["branch"] == "AI&ML"
    r4 = client.delete("/students/101")
    assert r4.status_code == 200 and len(students_db) == 0
    print("POST /students ->", r1.json())
    print("GET  /students ->", r2.json())
    print("PUT  /students/101 ->", r3.json())
    print("DELETE /students/101 ->", r4.json())
    print("All 4 assert test cases PASSED.")
