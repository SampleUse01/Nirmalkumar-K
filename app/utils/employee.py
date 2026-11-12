from fastapi import APIRouter
from app.database import db
from app.schemas.employee import EmployeeCreate

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post("/")
async def create_employee(employee: EmployeeCreate):

    result = await db.employees.insert_one(
        employee.model_dump()
    )

    return {
        "success": True,
        "id": str(result.inserted_id)
    }

@router.get("/")
async def get_employees():

    employees = []

    async for emp in db.employees.find():

        emp["_id"] = str(emp["_id"])

        employees.append(emp)

    return employees

from bson import ObjectId

@router.get("/{id}")
async def get_employee(id: str):

    employee = await db.employees.find_one(
        {"_id": ObjectId(id)}
    )

    if employee:

        employee["_id"] = str(employee["_id"])

    return employee

@router.put("/{id}")
async def update_employee(
    id: str,
    employee: EmployeeCreate
):

    await db.employees.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": employee.model_dump()
        }
    )

    return {
        "success": True
    }

@router.delete("/{id}")
async def delete_employee(id: str):

    await db.employees.delete_one(
        {"_id": ObjectId(id)}
    )

    return {
        "success": True
    }