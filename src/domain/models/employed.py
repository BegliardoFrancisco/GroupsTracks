from datetime import datetime


class Employed:
    def __init__(self, id: int, last_name: str, first_name: str, title: str,
                 birthdate: datetime, hiredate: datetime, address: str, city: str, state: str, country: str,
                 postalcode: str, phone: str, fax: str, email: str, reports_to=None):

        self.id: int = id
        self.lastName: str = last_name
        self.firstName: str = first_name
        self.title: str = title
        self.reportsTo: Employed = reports_to
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
