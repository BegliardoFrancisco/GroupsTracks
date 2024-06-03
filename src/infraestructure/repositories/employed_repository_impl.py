import asyncio
from src.domain.models.employed import Employed
from src.infraestructure.entities.employeesDAO import EmployesDAO
from src.domain.repositories.employed_repository import EmployedRepositories
from typing import List
from sqlalchemy import select, delete, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.repositories.customers_repository import CustomerRepositories
from src.infraestructure.repositories import engine


class EmployedRepositoryImpl(EmployedRepositories):

    def __init__(self, customer_repository: CustomerRepositories) -> None:
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        self.customer_repository = customer_repository

    async def get_all_employed(self, ) -> List[Employed]:
        try:
            async with self.async_session() as session:
                query = select(EmployesDAO)
                employees: List[EmployesDAO] = (await session.execute(query)).scalars().all()

                if not employees:
                    raise ConnectionError(f"I don't know i can perform "
                                          f"the search or this has not returned results")

                tasks = [employed.from_domain() for employed in employees]
                results: List[Employed] = await asyncio.gather(*tasks)

                return results
        except Exception as e:
            print(f"Error in get_all_employed: {e}")
            return []

    async def get_employed_by_id(self, employed_id: int) -> Employed:
        try:
            if not isinstance(employed_id, int):
                raise AttributeError(f"employed_id not is instance of int")

            async with self.async_session() as session:
                query = select(EmployesDAO).where(EmployesDAO.EmployeeId == employed_id)

                employed, *_ = (await session.execute(query)).scalars().all()

                if not employed:
                    raise ConnectionError(f"I don't know i can perform "
                                          f"the search or this has not returned results")

                return await employed.from_domain()

        except Exception as e:
            print(f"Error in get_employed_by_id: {e}")
            raise e

    async def add_employed(self, employed: Employed) -> None:
        try:
            if not isinstance(employed, Employed):
                raise AttributeError(f"thee album prop in methods not is type Employed")

            async with self.async_session() as session:
                async with session.begin():
                    session.add(await EmployesDAO.from_dto(employed))
        except Exception as e:
            print(f"Error in add_employed: {str(e)}")
            raise e

    async def update_employed(self, employed: Employed) -> None:
        try:
            async with self.async_session() as session:
                async with session.begin():
                    # Fetch the specific album object using fetchone
                    result = await session.execute(
                        select(EmployesDAO).filter(EmployesDAO.EmployeeId == employed.id)
                    )
                    album_from_db = result.scalar()

                    # Check if album was found
                    if not album_from_db:
                        raise ValueError(f"Artist with ID {id} not found")

                    # If the object is a SQLAlchemy model, update it using the update() method
                    if isinstance(album_from_db, EmployesDAO):

                        id_leader: int | None = employed.reportsTo.id if employed.reportsTo else None

                        await session.execute(
                            update(EmployesDAO)
                            .where(EmployesDAO.EmployeeId == employed.id)
                            .values({
                                EmployesDAO.EmployeeId: employed.id,
                                EmployesDAO.LastName: employed.lastName,
                                EmployesDAO.FirstName: employed.firstName,
                                EmployesDAO.Title: employed.title,
                                EmployesDAO.ReportsTo: id_leader,
                                EmployesDAO.BirthDate: employed.birthDate,
                                EmployesDAO.HireDate: employed.hireDate,
                                EmployesDAO.Address: employed.address,
                                EmployesDAO.City: employed.city,
                                EmployesDAO.State: employed.state,
                                EmployesDAO.Country: employed.country,
                                EmployesDAO.PostalCode: employed.postalCode,
                                EmployesDAO.Phone: employed.phone,
                                EmployesDAO.Fax: employed.fax,
                                EmployesDAO.Email: employed.email
                            })
                        )
        except Exception as e:
            raise e

    async def delete_employed(self, employed_id) -> None:
        try:

            if not isinstance(employed_id, int):
                raise AttributeError(f"employed_id no is instance of int")

            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(EmployesDAO)
                        .where(EmployesDAO.EmployeeId == employed_id)
                    )
        except Exception as e:
            print(f"Error in delete_album: {str(e)}")
            raise e
