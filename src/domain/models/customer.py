from .employed import Employed
from typing import List
from .invoice import Invoice


class Customer:

    def __init__(self, id: int, last_name: str, first_name: str, company: str,
                 address: str, city: str, state: str, country: str, postal_code: str,
                 phone: str, fax: str, email: str, support_rep: Employed, invoices: List[Invoice] | None = None):
        self.id: int = id
        self.lastName: str = last_name
        self.firstName: str = first_name
        self.company: str = company
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.country: str = country
        self.postalCode: str = postal_code
        self.phone: str = phone
        self.fax: str = fax
        self.email: str = email
        self.supportRep: Employed = support_rep
        self.invoices: List[Invoice] = invoices if invoices is not None else []

    def add_invoice(self, invoice: Invoice):
        if isinstance(invoice, Invoice):
            self.invoices.append(invoice)
        else:
            raise TypeError(f"the invoice argument no is type Invoice is type:{type(invoice)}"
                           + f"class:{__class__} in {__name__} {__file__}")
