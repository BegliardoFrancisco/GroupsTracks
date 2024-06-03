import asyncio
from src.domain.models.invoice_items import InvoiceItems
from src.infraestructure.entities.invoice_itemsDAO import InvoiceItemsDAO
from src.domain.repositories.invoice_item_repository import InvoiceItemRepositories
from typing import List
from sqlalchemy import select, delete, update
from sqlalchemy.orm import sessionmaker, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine


class InvoiceItemRepositoryImpl(InvoiceItemRepositories):

    def __init__(self,) -> None:
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_invoice_item(self) -> List[InvoiceItems]:
        try:
            async with self.async_session() as session:
                query = select(InvoiceItemsDAO)
                invoices_item: List[InvoiceItemsDAO] = (await session.execute(query)).scalars().all()

                if not invoices_item or invoices_item == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_item_domain: List[InvoiceItems] = await asyncio.gather(*[
                    item.from_domain()
                    for item in invoices_item
                ])
                return invoices_item_domain

        except Exception as e:
            print(f"Error in get_all_invoice_item: {e}")
            raise e

    async def get_invoice_item_by_id(self, invoice_item_id: int) -> InvoiceItems:
        try:
            if not isinstance(invoice_item_id, int):
                raise AttributeError(f"invoice_item_id no is instance of int type")

            async with (self.async_session() as session):
                query = (
                    select(InvoiceItemsDAO)
                    .where(InvoiceItemsDAO.InvoiceLineId == invoice_item_id)
                    )

                invoice_item, *_ = (await session.execute(query)).scalars().all()

                if not invoice_item:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                return await invoice_item.from_domain()
        except Exception as e:
            print(f"Error in get_invoice_item_by_id: {e}")
            raise e

    async def get_invoice_item_from_invoice_id(self, invoice_id: int) -> List[InvoiceItems]:
        try:
            if not isinstance(invoice_id, int):
                raise AttributeError(f"invoice_id no is instance of int")

            async with self.async_session() as session:
                query = (
                    select(InvoiceItemsDAO)
                    .where(InvoiceItemsDAO.InvoiceId == invoice_id)
                    .options(
                        selectinload(InvoiceItemsDAO.track)
                    ))

                invoices_item: List[InvoiceItemsDAO] = (await session.execute(query)).scalars().all()

                if not invoices_item:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_item_domain: List[InvoiceItems] = await asyncio.gather(*[
                    item.from_domain()
                    for item in invoices_item
                ])

                return invoices_item_domain
        except Exception as e:
            print(f"Error in get_invoice_item_from_invoice_id: {e}")
            raise e

    async def add_invoice_item(self, invoice_item: InvoiceItems, invoice_id: int) -> None:

        try:
            if not isinstance(invoice_id, int):
                raise ValueError(f" invoice_id incorrect type for the add_invoice_item method ")
            if not isinstance(invoice_item, InvoiceItems):
                raise ValueError(f"provides incorrect data for the add_invoice_item method")

            async with self.async_session() as session:
                async with session.begin():
                    item = await InvoiceItemsDAO.from_dto(invoice_item, invoice_id)
                    session.add(
                        item
                    )
        except Exception as e:
            print(f"Error in add_invoice_item: {e}")
            raise e

    async def add_invoices_items(self, invoices_items: List[InvoiceItems], invoice_id: int) -> None:

        try:
            if not isinstance(invoice_id, int):
                raise ValueError(f" invoice_id incorrect type for the add_invoice_item method ")
            if not isinstance(invoices_items, List):
                raise ValueError(f"provides incorrect data for the add_invoices_items method")

            async with self.async_session() as session:
                async with session.begin():
                    session.add_all(
                        await asyncio.gather(*[
                            InvoiceItemsDAO.from_dto(invoice_item, invoice_id)
                            for invoice_item in invoices_items
                        ])
                    )
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
                                InvoiceItemsDAO.InvoiceId: invoice_id,
                                InvoiceItemsDAO.TrackId: invoice_item.track.id,
                                InvoiceItemsDAO.UnitPrice: invoice_item.unitPrice,
                                InvoiceItemsDAO.Quantity: invoice_item.quantity
                            })
                        )
        except Exception as e:
            raise e

    async def delete_invoice_item(self, invoice_item_id: int) -> None:
        try:
            if not isinstance(invoice_item_id, int):
                raise AttributeError(f"id no is instance of int")

            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(InvoiceItemsDAO)
                        .where(InvoiceItemsDAO.InvoiceLineId == invoice_item_id)
                    )
        except Exception as e:
            print(f"Error in delete_invoice_item: {str(e)}")
            raise e
