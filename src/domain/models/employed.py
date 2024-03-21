from datetime import datetime
from typing import Optional


class Employed:
    def __init__(self, id: int, last_name: str, first_name: str, title: str,
                 birthdate: datetime, hiredate: datetime, address: str, city: str, state: str, country: str,
                 postalcode: str, phone: str, fax: str, email: str, reports_to: Optional['Employed']):

        self.id: int = id
        self.lastName: str = last_name
        self.firstName: str = first_name
        self.title: str = title
        self.reportsTo: Optional[Employed] = reports_to if not None else None
        self.birthDate: datetime = birthdate
        self.hireDate: datetime = hiredate
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.country: str = country
        self.postalCode: str = postalcode
        self.phone: str = phone
        self.fax: str = fax
        self.email: str = email

    async def set_reports_to(self, leader: Optional['Employed']):
        self.reportsTo = leader
