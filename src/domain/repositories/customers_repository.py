from src.domain.models.customer import Customer
from typing import List
from abc import ABC, abstractmethod


class CustomerRepositories(ABC):

    @abstractmethod
    async def get_all_customers(self, ) -> List[Customer]:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_all_customers is abstract method in {__class__}")

    @abstractmethod
    async def get_customers_by_id(self, id: int) -> Customer:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_customers_by_id is abstract method in {__class__}")

    @abstractmethod
    async def get_customers_by_employed(self, employed_id: int) -> List[Customer]:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_customers_by_employed is abstract method in {__class__}")

    @abstractmethod
    async def add_customers(self, customers: Customer, support_id: int) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"add_customers is abstract method in {__class__}")

    @abstractmethod
    async def update_customers(self, customers: Customer, employed_id: int) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"update_customers is abstract method in {__class__}")

    @abstractmethod
    async def delete_customers(self, customers_id) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"delete_customers is abstract method in {__class__}")
