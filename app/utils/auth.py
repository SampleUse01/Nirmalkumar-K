from fastapi import APIRouter
from app.database import db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
async def login(payload: dict):

    user = await db.users.find_one(
        {
            "email": payload["email"]
        }
    )

    if not user:
        return {
            "success": False,
            "message": "Invalid Credentials"
        }

    if user["password"] != payload["password"]:
        return {
            "success": False,
            "message": "Invalid Credentials"
        }

    return {
        "success": True,
        "role": user["role"],
        "email": user["email"]
    }