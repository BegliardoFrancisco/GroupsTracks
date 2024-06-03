from src.infraestructure.entities.base import Base
from src.domain.models.invoice import Invoice
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime


class CustomerDAO:
    pass


class InvoicesDAO(Base):
    __tablename__ = "invoices"
    InvoiceId: Mapped[int] = mapped_column(primary_key=True)
    CustomerId: Mapped[int] = mapped_column(ForeignKey("customers.CustomerId"))
    InvoiceDate: Mapped[datetime]
    BillingAddress: Mapped[str]
    BillingCity: Mapped[str]
    BillingState: Mapped[str]
    BillingCountry: Mapped[str]
    BillingPostalCode: Mapped[str]
    Total: Mapped[int]
    customer = relationship("CustomersDAO", back_populates="invoices", lazy='selectin')

    async def from_domain(self) -> Invoice:
        return Invoice(
            id=self.InvoiceId,
            date=self.InvoiceDate,
            address=self.BillingAddress,
            city=self.BillingCity,
            state=self.BillingState,
            country=self.BillingCountry,
            postalcode=self.BillingPostalCode,
            price_total=self.Total,
            items=None
        )

    @staticmethod
    async def from_dto(invoice: Invoice, customer_id) -> 'InvoicesDAO':
        return InvoicesDAO(
            InvoiceId=invoice.id,
            CustomerId=customer_id,
            InvoiceDate=invoice.date,
            BillingAddress=invoice.address,
            BillingCity=invoice.city,
            BillingState=invoice.state,
            BillingCountry=invoice.country,
            BillingPostalCode=invoice.postalCode,
            Total=invoice.price_total,
        )
