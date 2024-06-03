import asyncio

from src.domain.models.invoice import Invoice
from src.domain.repositories.Invoice_repository import InvoiceRepositories
from src.domain.models.invoice_items import InvoiceItems
from src.domain.repositories.invoice_item_repository import InvoiceItemRepositories
from src.infraestructure.entities.invoice_itemsDAO import InvoiceItemsDAO
from src.infraestructure.entities.invoicesDAO import InvoicesDAO
from typing import List
from sqlalchemy import select, delete, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine


class InvoiceRepositoryImpl(InvoiceRepositories):

    def __init__(self, invoice_items_repository: InvoiceItemRepositories) -> None:
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        self.invoices_items_repository = invoice_items_repository

    async def get_all_invoice(self) -> List[Invoice]:
        try:
            async with self.async_session() as session:
                query = select(InvoicesDAO)
                invoices: List[InvoicesDAO] = (await session.execute(query)).scalars().all()  # List[InvoiceItemsDAO]

                if not invoices:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_domain: List[Invoice] = await asyncio.gather(*[
                    invoice.from_domain()
                    for invoice in invoices
                ])

                return invoices_domain
        except Exception as e:
            print(f"Error in get_all_invoice_item: {e}")
            raise e

    async def get_invoice_by_id(self, invoice_id: int) -> Invoice:
        try:
            if not isinstance(invoice_id, int):
                raise AttributeError(f"invoice_id no is instance of int")

            async with (self.async_session() as session):
                query = select(InvoicesDAO).where(InvoicesDAO.InvoiceId == invoice_id)
                invoice, *_ = (await session.execute(query)).scalars().all()

                if not invoice:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_item = await self.invoices_items_repository.get_invoice_item_from_invoice_id(invoice.InvoiceId)
                invoice_domain: Invoice = await invoice.from_domain()
                await invoice_domain.add_items(invoices_item)

                return invoice_domain
        except Exception as e:
            print(f"Error in get_invoice_item_by_id: {e}")
            raise e

    async def get_invoice_by_customer_id(self, customer_id: int) -> List[Invoice]:
        try:
            if not isinstance(customer_id, int):
                raise AttributeError(f"customer_id no is instance of int")

            async with (self.async_session() as session):

                query = (select(InvoicesDAO)
                         .where(InvoicesDAO.CustomerId == customer_id)
                         )

                invoices: List[InvoicesDAO] = (await session.execute(query)).scalars().all()  # List[InvoiceItemsDAO]

                if not invoices:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_domain: List[Invoice] = await asyncio.gather(*[
                    self.parser_invoice_with_item(invoice)
                    for invoice in invoices
                ])

                return invoices_domain
        except Exception as e:
            print(f"Error in get_invoice_item_by_id: {e}")
            raise e

    async def parser_invoice_with_item(self, invoice: InvoicesDAO) -> Invoice:

        items: List[InvoiceItems] = (
            await self.invoices_items_repository
            .get_invoice_item_from_invoice_id(invoice.InvoiceId)
        )
        invoice_domain: Invoice = await invoice.from_domain()

        await invoice_domain.add_items(items)

        return invoice_domain

    async def add_invoice(self, invoice: Invoice, customer_id: int) -> None:
        try:
            if not isinstance(customer_id, int):
                raise ValueError(f" customer_id incorrect type for the add_invoice method ")
            if not isinstance(invoice, Invoice):
                raise ValueError(f"provides incorrect data for the add_invoice method")

            async with self.async_session() as session:
                async with session.begin():
                    invoice_dto = await InvoicesDAO.from_dto(invoice, customer_id)

                    session.add(
                        invoice_dto
                    )

                    if invoice.items:
                        invoices_items_dto: List[InvoiceItemsDAO] = await asyncio.gather(*[
                            InvoiceItemsDAO.from_dto(item, invoice.id)
                            for item in invoice.items
                        ])
                        session.add_all(
                            invoices_items_dto
                        )
        except Exception as e:
            print(f"Error in add_invoice_item: {e}")
            raise e

    async def update_invoice(self, invoice: Invoice, customer_id: int) -> None:
        try:

            if not isinstance(invoice, Invoice):
                raise ValueError(f"Error in method update_invoice: don't provides params from type Artist")

            async with self.async_session() as session:
                async with session.begin():
                    # Fetch the specific invoice_item object using fetchone
                    result = await session.execute(
                        select(InvoicesDAO).filter(InvoicesDAO.InvoiceId == invoice.id)
                    )
                    invoice_item_from_db = result.scalar()

                    # Check if invoice_item was found
                    if not invoice_item_from_db:
                        raise ValueError(f"Invoice_item with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(invoice_item_from_db, InvoicesDAO):
                        await session.execute(
                            update(InvoicesDAO)
                            .where(InvoicesDAO.InvoiceId == invoice.id)
                            .values({
                                InvoicesDAO.InvoiceId: invoice.id,
                                InvoicesDAO.CustomerId: customer_id,
                                InvoicesDAO.InvoiceDate: invoice.date,
                                InvoicesDAO.BillingAddress: invoice.address,
                                InvoicesDAO.BillingCity: invoice.city,
                                InvoicesDAO.BillingState: invoice.state,
                                InvoicesDAO.BillingCountry: invoice.country,
                                InvoicesDAO.BillingPostalCode: invoice.postalCode,
                                InvoicesDAO.Total: invoice.price_total,
                            })
                        )
        except Exception as e:
            raise e

    async def delete_invoice(self, invoice_id) -> None:
        try:
            if not isinstance(invoice_id, int):
                raise AttributeError(f"id no is instance of int")

            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(InvoicesDAO)
                        .where(InvoicesDAO.InvoiceId == invoice_id)
                    )
        except Exception as e:
            print(f"Error in delete_invoice: {str(e)}")
            raise e
