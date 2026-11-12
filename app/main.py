from fastapi import FastAPI
from app.utils import auth
from app.utils import employee
from app.utils import dashboard

app = FastAPI()

app.include_router(auth.router)
app.include_router(employee.router)
app.include_router(dashboard.router)

@app.get("/")
def root():
    return {
        "message": "Workforce Management API"
    }