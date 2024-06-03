from src.domain.models.customer import Customer
from src.infraestructure.entities.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey


class CustomersDAO(Base):
    __tablename__ = "customers"

    CustomerId: Mapped[int] = mapped_column(primary_key=True)
    LastName: Mapped[str]
    FirstName: Mapped[str]
    Company: Mapped[str]
    Address: Mapped[str]
    City: Mapped[str]
    State: Mapped[str]
    Country: Mapped[str]
    PostalCode: Mapped[str]
    Phone: Mapped[str]
    Fax: Mapped[str]
    Email: Mapped[str]
    SupportRepId: Mapped[int] = mapped_column(ForeignKey("employees.EmployeeId"))
    # foreing error is upper firts char tho string
    invoices = relationship("InvoicesDAO", back_populates="customer", lazy='selectin')

    async def from_domain(self) -> Customer:
        inv = [await invoice.from_domain() for invoice in self.invoices]
        return Customer(
            id=self.CustomerId,
            last_name=self.LastName,
            first_name=self.FirstName,
            company=self.Company,
            address=self.Address,
            city=self.City,
            state=self.State,
            country=self.Country,
            postal_code=self.PostalCode,
            phone=self.Phone,
            fax=self.Fax,
            email=self.Email,
            invoices=inv
        )

    @staticmethod
    async def from_dto(customer: Customer, suport_id: int) -> 'CustomersDAO':
        return CustomersDAO(
            CustomerId=customer.id,
            LastName=customer.lastName,
            FirstName=customer.firstName,
            Company=customer.company,
            Address=customer.address,
            City=customer.city,
            State=customer.state,
            Country=customer.country,
            PostalCode=customer.postalCode,
            Phone=customer.phone,
            Fax=customer.fax,
            Email=customer.email,
            SupportRepId=suport_id
        )
