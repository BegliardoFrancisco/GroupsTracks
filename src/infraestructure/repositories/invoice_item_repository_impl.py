from src.domain.models.invoice_items import InvoiceItems
from src.domain.models.track import Track
from src.domain.repositories.track_repository import TrackRepository
from src.infraestructure.entities.invoice_itemsDAO import InvoiceItemsDAO
from src.domain.repositories.invoice_item_repository import InvoiceItemRepositories
from typing import List
from sqlalchemy import select, delete, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from pipe import Pipe


class InvoiceItemRepositoryImpl(InvoiceItemRepositories):

    def __init__(self, track_repository: TrackRepository) -> None:
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        self.track_repository = track_repository

    async def get_all_invoice_item(self) -> List[InvoiceItems]:
        try:
            async with self.async_session() as session:
                query = select(InvoiceItemsDAO)
                invoices_item: List[InvoiceItemsDAO] = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all()))  # List[InvoiceItemsDAO]

                if not invoices_item | invoices_item == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_item_domain: List[InvoiceItems]
                for invoice_item in invoices_item:
                    track_to_item: Track = await self.track_repository.get_track_by_id(invoice_item.TrackId)
                    invoices_item_domain.append(InvoiceItems(
                        invoice_item.InvoiceId,
                        track_to_item,
                        invoice_item.UnitPrice,
                        invoice_item.Quantity
                    ))
                return invoices_item_domain
        except Exception as e:
            print(f"Error in get_all_invoice_item: {e}")
            raise e

    async def get_invoice_item_by_id(self, invoice_item_id: int) -> InvoiceItems:
        try:
            if not isinstance(invoice_item_id, int) or not isinstance(invoice_item_id, float):
                raise AttributeError(f"invoice_item_id no is instance of int or float type")

            async with (self.async_session() as session):
                query = select(InvoiceItemsDAO).where(InvoiceItemsDAO.InvoiceLineId == invoice_item_id)
                invoice_item: InvoiceItemsDAO = await (session.execute(query)
                                                       ).execute.scalars().all()  # List[InvoiceItemsDAO]

                if not invoice_item | invoice_item == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                track_to_item: Track = await self.track_repository.get_track_by_id(invoice_item.TrackId)
                invoice_item_domain: InvoiceItems = InvoiceItems(
                    invoice_item.InvoiceId,
                    track_to_item,
                    invoice_item.UnitPrice,
                    invoice_item.Quantity
                )
                return invoice_item_domain
        except Exception as e:
            print(f"Error in get_invoice_item_by_id: {e}")
            raise e

    async def get_invoice_item_from_invoice_id(self, invoice_id: int) -> List[InvoiceItems]:
        try:
            if not isinstance(invoice_id, int) or not isinstance(invoice_id, float):
                raise AttributeError(f"invoice_id no is instance of int or float type")

            async with self.async_session() as session:
                query = select(InvoiceItemsDAO).where(InvoiceItemsDAO.InvoiceId == invoice_id)
                invoices_item: List[InvoiceItemsDAO] = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all()))  # List[InvoiceItemsDAO]

                if not invoices_item | invoices_item == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_item_domain: List[InvoiceItems]
                for invoice_item in invoices_item:
                    track_to_item: Track = await self.track_repository.get_track_by_id(invoice_item.TrackId)
                    invoices_item_domain.append(InvoiceItems(
                        invoice_item.InvoiceId,
                        track_to_item,
                        invoice_item.UnitPrice,
                        invoice_item.Quantity
                    ))
                return invoices_item_domain
        except Exception as e:
            print(f"Error in get_invoice_item_from_invoice_id: {e}")
            raise e

    async def add_invoice_item(self, invoice_item: InvoiceItems, invoice_id: int) -> None:

        try:
            if not isinstance(invoice_id, int) or not isinstance(invoice_id, float):
                raise ValueError(f" invoice_id incorrect type for the add_invoice_item method ")
            if not isinstance(invoice_item, InvoiceItems):
                raise ValueError(f"provides incorrect data for the add_invoice_item method")

            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        InvoiceItemsDAO(InvoiceLineId=invoice_item.id,
                                        InvoiceId=invoice_id,
                                        TrackId=invoice_item.track.id,
                                        UnitPrice=invoice_item.unitPrice,
                                        Quantity=invoice_item.quantity)
                    ])
        except Exception as e:
            print(f"Error in add_invoice_item: {e}")
            raise e

    async def update_invoice_item(self, invoice_item: InvoiceItems, invoice_id: int) -> None:
        try:

            if not isinstance(invoice_item, InvoiceItems):
                raise ValueError(f"Error in method update_invoice_item: don't provides params from type Artist")

            async with self.async_session() as session:
                async with session.begin():
                    # Fetch the specific invoice_item object using fetchone
                    result = await session.execute(
                        select(InvoiceItemsDAO).filter(InvoiceItemsDAO.InvoiceLineId == invoice_item.id)
                    )
                    invoice_item_from_db = result.scalar()

                    # Check if invoice_item was found
                    if not invoice_item_from_db:
                        raise ValueError(f"Invoice_item with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(invoice_item_from_db, InvoiceItemsDAO):
                        await session.execute(
                            update(InvoiceItemsDAO)
                            .where(InvoiceItemsDAO.InvoiceLineId == invoice_item.id)
                            .values({
                                InvoiceItemsDAO.InvoiceLineId: invoice_item.id,
                                InvoiceItemsDAO.TrackID: invoice_item.track.id,
                                InvoiceItemsDAO.UnitPrice: invoice_item.unitPrice,
                                InvoiceItemsDAO.Quantity: invoice_item.quantity
                            })
                        )
        except Exception as e:
            raise e

    async def delete_invoice_item(self, invoice_item_id: int) -> None:
        try:
            if not isinstance(id, int) or not isinstance(id, float):
                raise AttributeError(f"id no is instance of int or float type")

            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(InvoiceItemsDAO)
                        .where(InvoiceItemsDAO.InvoiceLineId == invoice_item_id)
                    )
        except Exception as e:
            print(f"Error in delete_invoice_item: {str(e)}")
            raise e
