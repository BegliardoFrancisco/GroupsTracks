from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime


class EmployeesDAO(Base):

    ___tablename__ = "employees"
    EmployeeId: Mapped[int] = mapped_column(primary_key=True)
    LastName: Mapped[str]
    FirstName: Mapped[str]
    Title: Mapped[str]
    ReportsTo: Mapped[int] = mapped_column(ForeignKey("employees.EmployeeId"))
    BirthDate: Mapped[datetime]
    HireDate: Mapped[datetime]
    Address: Mapped[str]
    City: Mapped[str]
    State: Mapped[str]
    Country: Mapped[str]
    PostalCode: Mapped[str]
    Phone: Mapped[str]
    Fax: Mapped[str]
    Email: Mapped[str]
