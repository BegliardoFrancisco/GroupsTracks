from src.infraestructure.entities.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class InvoiceItemsDAO(Base):
    __tablename__ = "invoice_items"
    InvoiceLineId: Mapped[int] = mapped_column(primary_key=True)
    InvoiceId: Mapped[int] = mapped_column(ForeignKey("invoices.InvoiceId"))
    TrackID: Mapped[int] = mapped_column(ForeignKey("tracks.TrackId"))
    UnitPrice: Mapped[int]
    Quantity: Mapped[int]


