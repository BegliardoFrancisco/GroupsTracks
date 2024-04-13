from src.domain.models.invoice import Invoice
from src.domain.repositories.Invoice_repository import InvoiceRepositories
from src.domain.repositories.invoice_item_repository import InvoiceItemRepositories
from src.infraestructure.entities.invoicesDAO import InvoicesDAO
from typing import List
from sqlalchemy import select, delete, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from pipe import Pipe


class InvoiceRepositoryImpl(InvoiceRepositories):

    def __init__(self, invoice_items_repository: InvoiceItemRepositories) -> None:
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        self.invoices_items_repository = invoice_items_repository

    async def get_all_invoice(self) -> List[Invoice]:
        try:
            async with self.async_session() as session:
                query = select(InvoicesDAO)
                invoices: List[InvoicesDAO] = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all()))  # List[InvoiceItemsDAO]

                if not invoices | invoices == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_domain: List[Invoice]
                for invoice in invoices:
                    invoices_items = await self.invoices_items_repository.get_invoice_item_from_invoice_id(
                        invoice.InvoiceId)
                    invoices_domain.append(Invoice(
                        invoice.InvoiceId,
                        invoice.InvoiceDate,
                        invoice.BillingAddress,
                        invoice.BillingCity,
                        invoice.BillingState,
                        invoice.BillingCountry,
                        invoice.BillingPostalCode,
                        invoice.Total,
                        invoices_items
                    ))
                return invoices_domain
        except Exception as e:
            print(f"Error in get_all_invoice_item: {e}")
            raise e

    async def get_invoice_by_id(self, invoice_id: int) -> Invoice:
        try:
            if not isinstance(invoice_id, int) or not isinstance(invoice_id, float):
                raise AttributeError(f"invoice_id no is instance of int or float type")

            async with (self.async_session() as session):
                query = select(InvoicesDAO).where(InvoicesDAO.InvoiceId == invoice_id)
                invoice: InvoicesDAO = await (session.execute(query)
                                              ).execute.scalars().all()  # List[InvoiceItemsDAO]

                if not invoice | invoice == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_item = await self.invoices_items_repository.get_invoice_item_from_invoice_id(invoice.InvoiceId)
                invoice_domain: Invoice = Invoice(
                    invoice.InvoiceId,
                    invoice.InvoiceDate,
                    invoice.BillingAddress,
                    invoice.BillingCity,
                    invoice.BillingState,
                    invoice.BillingCountry,
                    invoice.BillingPostalCode,
                    invoice.Total,
                    invoices_item
                )
                return invoice_domain
        except Exception as e:
            print(f"Error in get_invoice_item_by_id: {e}")
            raise e

    async def get_invoice_by_customer_id(self, customer_id: int) -> List[Invoice]:
        try:
            if not isinstance(customer_id, int) or not isinstance(customer_id, float):
                raise AttributeError(f"customer_id no is instance of int or float type")

            async with (self.async_session() as session):
                query = select(InvoicesDAO).where(InvoicesDAO.CustomerId == customer_id)
                invoices: List[InvoicesDAO] = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all()))  # List[InvoiceItemsDAO]

                if not invoices | invoices == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices_domain: List[Invoice]

                for invoice in invoices:
                    invoices_items = await self.invoices_items_repository.get_invoice_item_from_invoice_id(
                        invoice.InvoiceId)
                    invoices_domain.append(Invoice(
                        invoice.InvoiceId,
                        invoice.InvoiceDate,
                        invoice.BillingAddress,
                        invoice.BillingCity,
                        invoice.BillingState,
                        invoice.BillingCountry,
                        invoice.BillingPostalCode,
                        invoice.Total,
                        invoices_items
                    ))
                return invoices_domain
        except Exception as e:
            print(f"Error in get_invoice_item_by_id: {e}")
            raise e

    async def add_invoice(self, invoice: Invoice, customer_id: int) -> None:
        try:
            if not isinstance(customer_id, int) or not isinstance(customer_id, float):
                raise ValueError(f" customer_id incorrect type for the add_invoice method ")
            if not isinstance(invoice, Invoice):
                raise ValueError(f"provides incorrect data for the add_invoice method")

            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        InvoicesDAO(
                            InvoiceId=invoice.id,
                            CustomerId=customer_id,
                            InvoiceDate=invoice.date,
                            BillingAddress=invoice.address,
                            BillingCity=invoice.city,
                            BillingState=invoice.state,
                            BillingCountry=invoice.country,
                            BillingPostalCode=invoice.postalCode,
                            Total=None,
                        )
                    ])
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
                                InvoicesDAO.Total: None,
                            })
                        )
        except Exception as e:
            raise e

    async def delete_invoice(self, invoice_id) -> None:
        try:
            if not isinstance(invoice_id, int) or not isinstance(invoice_id, float):
                raise AttributeError(f"id no is instance of int or float type")

            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(InvoicesDAO)
                        .where(InvoicesDAO.InvoiceId == invoice_id)
                    )
        except Exception as e:
            print(f"Error in delete_invoice: {str(e)}")
            raise e
