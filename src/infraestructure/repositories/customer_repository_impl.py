import asyncio
from src.domain.models.customer import Customer
from src.domain.repositories.customers_repository import CustomerRepositories
from src.domain.repositories.Invoice_repository import InvoiceRepositories
from src.infraestructure.entities.customersDAO import CustomersDAO
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from typing import List
from sqlalchemy import select, delete, update


class CustomerRespositoryImpl(CustomerRepositories):
    def __init__(self, invoice_repository) -> None:
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        self.invoice_repository: InvoiceRepositories = invoice_repository

    async def get_all_customers(self) -> List[Customer]:
        try:
            async with self.async_session() as session:
                query = select(CustomersDAO)
                customers: List[CustomersDAO] = (await session.execute(query)).scalars().all()

                if not customers:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                customers_domain: List[Customer] = await asyncio.gather(*[
                    customer.from_domain()
                    for customer in customers
                ])

                return customers_domain
        except Exception as e:
            print(f"Error in get_all_genres: {e}")
            raise e

    async def get_customers_by_id(self, id: int) -> Customer:
        try:
            async with self.async_session() as session:
                query = select(CustomersDAO).where(CustomersDAO.CustomerId == id)

                customer, *_ = (await session.execute(query)).scalars().all()  # List[CustomersDAO])

                if not customer:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                return await customer.from_domain()

        except Exception as e:
            print(f"Error in get_all_genres: {e}")
            raise e

    async def get_customers_by_employed(self, employed_id: int) -> List[Customer]:
        try:
            async with self.async_session() as session:
                query = select(CustomersDAO).where(CustomersDAO.SupportRepId == employed_id)

                customers: List[CustomersDAO] = (await session.execute(query)).scalars().all()

                if not customers:
                    raise ConnectionError(f"I don't know i can perform the search or this has not returned results")

                customers_domain: List[Customer] = await asyncio.gather(*[
                    customer.from_domain()
                    for customer in customers
                ])

                return customers_domain

        except Exception as e:
            print(f"Error in get_all_genres: {e}")
            raise e

    async def add_customers(self, customers: Customer, support_id: int) -> None:
        try:
            if not isinstance(customers, Customer):
                raise ValueError(f"It does´t an objet Customer")
            async with self.async_session() as session:
                async with session.begin():
                    customer = await CustomersDAO.from_dto(customers, support_id)
                    session.add(
                        customer
                    )
        except Exception as e:
            print(f"Error in add_customers: {e}")
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
                            .where(CustomersDAO.CustomerId == customer.id)
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
