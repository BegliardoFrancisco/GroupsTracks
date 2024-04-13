from src.domain.models.customer import Customer
from src.domain.repositories.customers_repository import CustomerRepositories
from src.domain.repositories.Invoice_repository import InvoiceRepositories
from src.infraestructure.entities.customersDAO import CustomersDAO
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from typing import List
from sqlalchemy import select, delete, update
from pipe import Pipe


class CustomerRespositoryImpl(CustomerRepositories):
    def __init__(self, invoice_repository) -> None:
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        self.invoice_repository: InvoiceRepositories = invoice_repository

    async def get_all_customers(self) -> List[Customer]:
        try:
            async with self.async_session() as session:
                query = select(CustomersDAO)
                customers = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all()))  # List[CustomersDAO])

                if not customers | customers == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                customers_domain: List[Customer]
                for customer in customers:
                    invoices = await self.invoice_repository.get_invoice_by_customer_id(customer.id)
                    customers_domain.append(Customer(
                        customer.id,
                        customer.lastName,
                        customer.firstName,
                        customer.company,
                        customer.address,
                        customer.city,
                        customer.state,
                        customer.country,
                        customer.postalCode,
                        customer.phone,
                        customer.fax,
                        customer.email,
                        invoices
                    ))
                return customers_domain
        except Exception as e:
            print(f"Error in get_all_genres: {e}")
            return []

    async def get_customers_by_id(self) -> Customer:
        try:
            async with self.async_session() as session:
                query = select(CustomersDAO)
                customer = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all()))  # List[CustomersDAO])

                if not customer | customer == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                invoices = await self.invoice_repository.get_invoice_by_customer_id(customer.id)
                customers_domain: Customer = Customer(
                    customer.id,
                    customer.lastName,
                    customer.firstName,
                    customer.company,
                    customer.address,
                    customer.city,
                    customer.state,
                    customer.country,
                    customer.postalCode,
                    customer.phone,
                    customer.fax,
                    customer.email,
                    invoices
                )
                return customers_domain

        except Exception as e:
            print(f"Error in get_all_genres: {e}")
            return []

    async def get_customers_by_employed(self, employed_id: int) -> List[Customer]:
        try:
            async with self.async_session() as session:
                query = select(CustomersDAO)
                customers = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all()))  # List[CustomersDAO])

                if not customers | customers == []:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                customers_domain: List[Customer]
                for customer in customers:
                    invoices = await self.invoice_repository.get_invoice_by_customer_id(customer.id)
                    customers_domain.append(Customer(
                        customer.id,
                        customer.lastName,
                        customer.firstName,
                        customer.company,
                        customer.address,
                        customer.city,
                        customer.state,
                        customer.country,
                        customer.postalCode,
                        customer.phone,
                        customer.fax,
                        customer.email,
                        invoices
                    ))

                return customers_domain

        except Exception as e:
            print(f"Error in get_all_genres: {e}")
            return []

    async def add_customers(self, customers: Customer, support_id: int) -> None:
        try:
            if not isinstance(customers, Customer):
                raise ValueError(f"It does´t an objet Customer")
            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([
                        CustomersDAO(
                            CustomerId=customers.id,
                            LastName=customers.lastName,
                            FirstName=customers.firstName,
                            Company=customers.company,
                            Address=customers.address,
                            City=customers.city,
                            State=customers.state,
                            Country=customers.country,
                            PostalCode=customers.postalCode,
                            Phone=customers.phone,
                            Fax=customers.fax,
                            Email=customers.email,
                            SupportRepId=support_id
                        )
                    ])
        except Exception as e:
            print(f"Error in add_genres: {e}")
            raise e

    async def update_customers(self, customer: Customer, employed_id: int) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    # Fetch the specific customers object using fetchone
                    result = await session.execute(
                        select(CustomersDAO).filter(CustomersDAO.CustomerId == customer.id)
                    )
                    customers_from_db = result.scalar()

                    # Check if album was found
                    if not customers_from_db:
                        raise ValueError(f"Artist with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(customers_from_db, CustomersDAO):
                        await session.execute(
                            update(CustomersDAO)
                            .where(CustomersDAO.EmployeeId == customer.id)
                            .values({
                                CustomersDAO.CustomerId: customer.id,
                                CustomersDAO.LastName: customer.lastName,
                                CustomersDAO.FirstName: customer.firstName,
                                CustomersDAO.Company: customer.company,
                                CustomersDAO.Address: customer.address,
                                CustomersDAO.City: customer.city,
                                CustomersDAO.State: customer.state,
                                CustomersDAO.Country: customer.country,
                                CustomersDAO.PostalCode: customer.postalCode,
                                CustomersDAO.Phone: customer.phone,
                                CustomersDAO.Fax: customer.fax,
                                CustomersDAO.Email: customer.email,
                                CustomersDAO.SupportRepId: employed_id
                            })
                        )
        except Exception as e:
            raise e

    async def delete_customers(self, customers_id) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    session.execute(
                        delete(CustomersDAO).where(CustomersDAO.CustomerId == customers_id)
                    )

        except Exception as e:
            print(f"Error in delete_genres: {e}")
            raise e
