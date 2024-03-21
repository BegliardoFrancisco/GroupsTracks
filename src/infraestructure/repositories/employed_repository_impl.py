from src.domain.models.employed import Employed
from src.infraestructure.entities.employeesDAO import EmployesDAO
from src.domain.repositories.employed_repository import EmployedRepositories
from typing import List, Optional
from sqlalchemy import select, delete, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.infraestructure.repositories import engine
from pipe import Pipe
from datetime import datetime


class CustomersRepositoryImpl(EmployedRepositories):

    def __init__(self) -> None:
        super().__init__()
        self.async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_employed(self, ) -> List[Employed]:
        try:
            async with self.async_session() as session:
                query = select(EmployesDAO)
                employees = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all())  # List[EmployesDAO]
                )
                if not employees | employees == []:
                    raise ConnectionError(f"I don't know i can perform "
                                          f"the search or this has not returned results")

                employees_domain: List[Employed]
                for employed in employees:
                    leader = await self.get_employed_by_id(employed.ReportsTo)
                    employees_domain.append(await self.employed_parser(
                        employed.EmployeeId,
                        employed.LastName,
                        employed.FirstName,
                        employed.Title,
                        employed.BirthDate,
                        employed.HireDate,
                        employed.Address,
                        employed.City,
                        employed.State,
                        employed.Country,
                        employed.PostalCode,
                        employed.Phone,
                        employed.Fax,
                        employed.Email,
                        leader))

                return employees_domain
        except Exception as e:
            print(f"Error in get_all_employed: {e}")
            return []

    async def get_employed_by_id(self, employed_id: int) -> Employed:
        try:
            if not isinstance(employed_id, int) or not isinstance(employed_id, int):
                raise AttributeError(f"artist_id no is instance of int or float type")

            async with self.async_session() as session:
                query = select(EmployesDAO).where(EmployesDAO.EmployeeId == employed_id)
                employees: List[EmployesDAO] = list(
                    await session.execute(query)  # List[Tuple]
                    | Pipe(lambda execute: execute.scalars().all()))  # List[EmployesDAO]

                if not employees | employees == []:
                    raise ConnectionError(f"I don't know i can perform "
                                          f"the search or this has not returned results")

                employee_domain: Employed
                for employed in employees:
                    leader = await self.get_employed_by_id(employed.ReportsTo)
                    employees_domain = await self.employed_parser(
                        employed.EmployeeId,
                        employed.LastName,
                        employed.FirstName,
                        employed.Title,
                        employed.BirthDate,
                        employed.HireDate,
                        employed.Address,
                        employed.City,
                        employed.State,
                        employed.Country,
                        employed.PostalCode,
                        employed.Phone,
                        employed.Fax,
                        employed.Email,
                        leader)

                return employees_domain

        except Exception as e:
            print(f"Error in get_employed_id: {e}")
            raise e

    async def add_employed(self, employed: Employed, leader_id: int) -> None:
        try:
            if not isinstance(employed.id, int) or not isinstance(employed.id, int):
                raise AttributeError(f"employed.id no is instance of int or float type")

            if not isinstance(employed, Employed) or not isinstance(employed, Employed):
                raise AttributeError(f"thee album prop in methods not is type Employed")

            async with self.async_session() as session:
                async with session.begin():
                    session.add_all([EmployesDAO(EmployeeId=employed.id,
                                                 LastName=employed.lastName,
                                                 FirstName=employed.firstName,
                                                 Title=employed.title,
                                                 ReportsTo=leader_id,
                                                 BirthDate=employed.birthDate,
                                                 HireDate=employed.hireDate,
                                                 Address=employed.address,
                                                 City=employed.city,
                                                 State=employed.state,
                                                 Country=employed.country,
                                                 PostalCode=employed.postalCode,
                                                 Phone=employed.phone,
                                                 Fax=employed.fax,
                                                 Email=employed.email)
                                     ])

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
                        await session.execute(
                            update(EmployesDAO)
                            .where(EmployesDAO.EmployeeId == employed.id)
                            .values({
                                EmployesDAO.EmployeeId: employed.id,
                                EmployesDAO.LastName: employed.lastName,
                                EmployesDAO.FirstName: employed.firstName,
                                EmployesDAO.Title: employed.title,
                                EmployesDAO.ReportsTo: employed.reportsTo.id,
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
            async with self.async_session() as session:
                async with session.begin():
                    await session.execute(
                        delete(EmployesDAO)
                        .where(EmployesDAO.EmployeeId == employed_id)
                    )
        except Exception as e:
            print(f"Error in delete_album: {str(e)}")
            raise e

    @staticmethod
    async def employed_parser(employed_id: int, last_name: str, first_name: str, title: str,
                              birth_date: datetime, hire_date: datetime, address: str, city: str, state: str,
                              country: str, postal_code: str, phone: str, fax: str, email: str,
                              leader: Optional['Employed']):
        return Employed(employed_id, last_name, first_name, title, birth_date, hire_date,
                        address, city, state, country, postal_code, phone, fax, email, leader)
