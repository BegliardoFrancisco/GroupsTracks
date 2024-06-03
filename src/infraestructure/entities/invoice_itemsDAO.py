from src.infraestructure.entities.base import Base
from src.infraestructure.entities.trackDAO import TrackDAO
from src.domain.models.invoice_items import InvoiceItems
from src.domain.models.track import Track
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey


class InvoiceItemsDAO(Base):
    __tablename__ = "invoice_items"
    InvoiceLineId: Mapped[int] = mapped_column(primary_key=True)
    InvoiceId: Mapped[int] = mapped_column(ForeignKey("invoices.InvoiceId"))
    TrackId: Mapped[int] = mapped_column(ForeignKey("tracks.TrackId"))
    UnitPrice: Mapped[int]
    Quantity: Mapped[int]
    track: Mapped['TrackDAO'] = relationship(lazy='selectin')

    async def from_domain(self) -> InvoiceItems:
        track: Track = await self.track.from_domain()
        return InvoiceItems(
            id=self.InvoiceLineId,
            track=track,
            price=self.UnitPrice,
            quantity=self.Quantity
        )

    @staticmethod
    async def from_dto(item: InvoiceItems, invoice_id: int) -> 'InvoiceItemsDAO':
        return InvoiceItemsDAO(
            InvoiceLineId=item.id,
            InvoiceId=invoice_id,
            TrackId=item.track.id,
            UnitPrice=item.unitPrice,
            Quantity=item.quantity
        )
