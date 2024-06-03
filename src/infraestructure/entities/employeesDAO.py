from typing import List
from src.domain.models.customer import Customer
from src.domain.models.employed import Employed
from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime


class EmployesDAO(Base):
    __tablename__ = "employees"

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
    customers = relationship("CustomersDAO", backref="supported", lazy='selectin')
    report: Mapped["EmployesDAO"] = relationship(backref="reports", lazy='selectin', remote_side=[EmployeeId])

    async def from_domain(self) -> Employed:
        cts: List[Customer] = [
            await c.from_domain()
            for c in self.customers]
        try:
            leader = await self.report.from_domain()
        except Exception as e:
            leader = None

        return Employed(
            id=self.EmployeeId,
            last_name=self.LastName,
            first_name=self.FirstName,
            title=self.Title,
            reports_to=leader,
            birthdate=self.BirthDate,
            hiredate=self.HireDate,
            address=self.Address,
            city=self.City,
            state=self.State,
            country=self.Country,
            postalcode=self.PostalCode,
            phone=self.Phone,
            fax=self.Fax,
            email=self.Email,
            customer=cts
        )

    @staticmethod
    async def from_dto(employed: Employed) -> 'EmployesDAO':

        id_leader:int | None = employed.reportsTo.id if (employed.reportsTo) else None

        return EmployesDAO(
            EmployeeId=employed.id,
            LastName=employed.lastName,
            FirstName=employed.firstName,
            Title=employed.title,
            ReportsTo=id_leader,
            BirthDate=employed.birthDate,
            HireDate=employed.hireDate,
            Address=employed.address,
            City=employed.city,
            State=employed.state,
            Country=employed.country,
            PostalCode=employed.postalCode,
            Phone=employed.phone,
            Fax=employed.fax,
            Email=employed.email,
        )
