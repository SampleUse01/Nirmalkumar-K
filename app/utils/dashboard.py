from fastapi import APIRouter

from app.database import db

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/super-admin")
async def super_admin_dashboard():

    totalEmployees = await db.employees.count_documents({})

    return {
        "totalEmployees": totalEmployees,
        "activeProjects": 12,
        "activeClients": 8,
        "billableHours": 2000
    }

@router.get("/employee")
async def employee_dashboard():

    return {

        "todayAttendance": "Present",

        "assignedProjects": 3,

        "pendingTimesheets": 1,

        "monthHours": 160,

        "billableHours": 140,

        "nonBillableHours": 20
    }