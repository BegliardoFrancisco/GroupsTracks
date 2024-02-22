from datetime import datetime
from typing import List
from .invoice_items import InvoiceItems
import asyncio


class Invoice:

    def __init__(self, id, date, address, city, state, country, postalcode, items: List[InvoiceItems]):
        self.id: int = id
        self.date: datetime = date
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.country: str = country
        self.postalCode: int = postalcode
        self.price_total: float = 0
        self.items: List[InvoiceItems] = items

    async def add_item(self, item: InvoiceItems) -> None:
        """
        Checking type for item and added in self.items: List
        :returns
            :typeError is item not type
            :None added invoice item in props items 

        """
        if isinstance(item, InvoiceItems):
            self.items.append(item)
        else:
            raise TypeError(f"the item argument not is type InvoiceItems, it is type {type(item)}"
                            +  f"class:{__class__} in {__name__} {__file__}")

    async def calculate_total_price(self) -> int:
        """
         creates a list of all unit prices and adds them up
        :return total price
        """
        prices_total = await asyncio.gather(*[
                                        item
                                        .calculate_total_item_price()
                                        for item in self.items]
                                      )
        return sum(prices_total)

    def set_price_total(self, price: float):
        if isinstance(price, int):
            self.price_total = price
        else:
            raise TypeError(f"the price argument no is type int, it is type {type(price)}" + 
                            "class:{__class__} in {__name__} {__file__}")
