import asyncio
from typing import List
from .invoice import Invoice


class Customer:

    def __init__(self, id: int, last_name: str, first_name: str, company: str,
                 address: str, city: str, state: str, country: str, postal_code: str,
                 phone: str, fax: str, email: str, invoices: List[Invoice] | None = None):
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
        self.invoices: List[Invoice] = invoices if invoices is not None else []

    def __str__(self):
        string = ('{'  
                        f' id: {self.id},\n'
                        f' lastname: {self.lastName},\n'
                        f' firstname: {self.firstName},\n'
                        f' email: {self.email},\n'
                        f' invoices: \n'
                  )

        cant_invoice = len(self.invoices) - 1
        count: int = 0
        while count <= cant_invoice:
            if count == cant_invoice:
                string += f' {self.invoices[count]},\n' + '}\n'

            string += f'  {self.invoices[count]},\n'
            count += 1
        return string + '\n}'

    async def add_invoice(self, invoice: Invoice):
        if isinstance(invoice, Invoice):
            self.invoices.append(invoice)
        else:
            raise TypeError(f"the invoice argument no is type Invoice is type:{type(invoice)}"
                            + f"class:{__class__} in {__name__} {__file__}")

    async def add_invoices(self, invoices: List[Invoice]):
        if isinstance(invoices, List):
            await asyncio.gather([await self.add_invoice(invoice) for invoice in invoices])
        else:
            raise TypeError(f"the invoice argument no is type List[Invoice] is type:{type(invoices)}"
                            + f"class:{__class__} in {__name__} {__file__}")
