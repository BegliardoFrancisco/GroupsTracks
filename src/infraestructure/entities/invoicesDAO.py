from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime


class InvoicesDAO(Base):

    __tablename__ = "invoices"
    InvoiceId: Mapped[int] = mapped_column(primary_key=True)
    CustomerId: Mapped[int] = mapped_column(ForeignKey("customers.CustomerId"))
    InvoicesId: Mapped[datetime]
    BillingAddress: Mapped[str]
    BillingCity: Mapped[str]
    BillingState: Mapped[str]
    BillingCountry: Mapped[str]
    BillingPostalCode: Mapped[str]
    Total: Mapped[int]
