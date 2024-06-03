from src.domain.models.employed import Employed
from abc import ABC, abstractmethod
from typing import List


class EmployedRepositories(ABC):

    @abstractmethod
    async def get_all_employed(self, ) -> List[Employed]:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_all_employed is abstract method in {__class__}")

    @abstractmethod
    async def get_employed_by_id(self, employed_id: int) -> Employed:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_employed_by_id is abstract method in {__class__}")

    @abstractmethod
    async def add_employed(self, employed: Employed) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"add_employed is abstract method in {__class__}")

    @abstractmethod
    async def update_employed(self, employed: Employed) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"update_employed is abstract method in {__class__}")

    @abstractmethod
    async def delete_employed(self, employed_id) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"delete_employed is abstract method in {__class__}")
