from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class CustomersDAO(Base):

    __tablename__ = "customers"
    CustomerId: Mapped[int] = mapped_column(primary_key=True)
    LastName: Mapped[str]
    FirstName: Mapped[str]
    Company:   Mapped[str]
    Address: Mapped[str]
    City: Mapped[str]
    State: Mapped[str]
    Country: Mapped[str]
    PostalCode: Mapped[str]
    Phone: Mapped[str]
    Fax: Mapped[str]
    Email: Mapped[str]
    SupportRepId: Mapped[int] = mapped_column(ForeignKey("Employees.EmployeeId"))
