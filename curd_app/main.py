from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
from database import sessionLocal, engine,Base 
import models,schemas,curd
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()


# dependency with the database
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

#endpoints
#1.create employee
@app.post("/employees", response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return curd.create_employee(db,employee)

#get all employees

@app.get("/employees", response_model = List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return curd.get_employees(db)


# get a specific empoyee

@app.get("/employees/{emp_id}", response_model = schemas.EmployeeOut)

def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = curd.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code = 404, detail="Employee not found")
    return employee

# update an employee

@app.put("/employees/{emp_id}", response_model = schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    employee_update = curd.update_employee(db, emp_id, employee)
    if employee_update is None:
        raise HTTPException(status_code = 404, detail="Employee not found")
    return employee_update

# 5. delete an employee

@app.delete("/employees/{emp_id}", response_model = dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = curd.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code = 404, detail="Employee not found")
    #return db_employee 
    # if this then response_model should be schemas.EmployeeOut else dict
    return {"detail": "Employee deleted successfully"}