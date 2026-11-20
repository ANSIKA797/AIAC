"""Employee Payroll RESTful API with documented endpoints."""
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(title="Employee Payroll API")
employees_db: dict[int, dict] = {}


class Employee(BaseModel):
    name: str
    department: str
    salary: float = Field(gt=0, description="Monthly salary must be positive")


class SalaryUpdate(BaseModel):
    salary: float = Field(gt=0)


@app.get("/employees")
def list_employees():
    """List all employees and their current salary details."""
    return {"employees": list(employees_db.values())}


@app.post("/employees", status_code=201)
def create_employee(emp_id: int, emp: Employee):
    """Register a new employee with initial salary details."""
    if emp_id in employees_db:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    employees_db[emp_id] = {"id": emp_id, **emp.dict()}
    return employees_db[emp_id]


@app.put("/employees/{emp_id}/salary")
def update_salary(emp_id: int, payload: SalaryUpdate):
    """Update the salary of an existing employee."""
    if emp_id not in employees_db:
        raise HTTPException(status_code=404, detail="Employee not found")
    employees_db[emp_id]["salary"] = payload.salary
    return employees_db[emp_id]


@app.delete("/employees/{emp_id}")
def remove_employee(emp_id: int):
    """Remove an employee from the payroll system."""
    if emp_id not in employees_db:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"deleted": employees_db.pop(emp_id)}


if __name__ == "__main__":
    client = TestClient(app)
    r1 = client.post("/employees?emp_id=501", json={"name": "Priya", "department": "Engineering", "salary": 75000})
    assert r1.status_code == 201 and r1.json()["salary"] == 75000
    r2 = client.put("/employees/501/salary", json={"salary": 85000})
    assert r2.status_code == 200 and r2.json()["salary"] == 85000
    r3 = client.get("/employees")
    assert r3.status_code == 200 and len(r3.json()["employees"]) == 1
    r4 = client.delete("/employees/501")
    assert r4.status_code == 200
    print("POST /employees ->", r1.json())
    print("PUT  /employees/501/salary ->", r2.json())
    print("GET  /employees ->", r3.json())
    print("DELETE /employees/501 ->", r4.json())
    print("All 4 assert test cases PASSED.")
