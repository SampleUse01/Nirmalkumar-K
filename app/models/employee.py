from sqlalchemy import *

from app.database import Base

class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer,primary_key=True)

    employee_id = Column(String(20))

    name = Column(String(100))

    email = Column(String(100))

    phone = Column(String(20))

    department = Column(String(100))

    designation = Column(String(100))

    manager = Column(String(100))

    role = Column(String(100))

    status = Column(String(20))