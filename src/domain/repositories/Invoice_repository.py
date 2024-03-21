from src.domain.models.invoice import Invoice
from typing import List
from abc import ABC, abstractmethod


class InvoiceRepositories(ABC):

    @abstractmethod
    def get_all_invoice(self, ) -> List[Invoice]:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_all_invoice is abstract method in {__class__}")

    @abstractmethod
    def get_invoice_by_id(self, invoice_id: int) -> Invoice:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"get_invoice_by_id is abstract method in {__class__}")

    @abstractmethod
    def add_invoice(self, invoice: Invoice) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"add_invoice is abstract method in {__class__}")

    @abstractmethod
    def update_invoice(self, invoice: Invoice) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"update_invoice is abstract method in {__class__}")

    @abstractmethod
    def delete_invoice(self, invoice_id) -> None:
        raise NotImplementedError(f"Not implemented Error:"
                                  + f"delete_invoice is abstract method in {__class__}")
