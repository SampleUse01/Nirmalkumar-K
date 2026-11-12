from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    employeeId: str
    name: str
    email: str
    phone: str
    department: str
    designation: str
    manager: str
    role: str
    status: str = "Active"