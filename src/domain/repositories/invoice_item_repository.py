from src.domain.models.invoice_items import InvoiceItems
from typing import List
from abc import ABC, abstractmethod


class InvoiceItemRepositories(ABC):

    @abstractmethod
    async def get_all_invoice_item(self, ) -> List[InvoiceItems]:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_all_invoice_item is abstract method in {__class__}")

    @abstractmethod
    async def get_invoice_item_by_id(self, invoice_item_id: int) -> InvoiceItems:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_invoice_item_by_id is abstract method in {__class__}")

    @abstractmethod
    async def get_invoice_item_from_invoice_id(self, invoice_id: int) -> List[InvoiceItems]:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_invoice_item_from_invoice_id is abstract method in {__class__}")

    @abstractmethod
    async def add_invoice_item(self, invoice_item: InvoiceItems, invoice_id: int) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"add_invoice_item is abstract method in {__class__}")

    @abstractmethod
    async def update_invoice_item(self, invoice_item: InvoiceItems, invoice_id: int) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"update_invoice_item is abstract method in {__class__}")

    @abstractmethod
    async def delete_invoice_item(self, invoice_item_id: int) -> None:
        raise NotImplementedError(f"Not implemented Error:" +
                                  f"delete_invoice_item is abstract method in {__class__}")
