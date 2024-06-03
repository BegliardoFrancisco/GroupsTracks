from datetime import datetime
from typing import List
from .invoice_items import InvoiceItems
import asyncio


class Invoice:

    def __init__(self, id, date, address, city,
                 state, country, postalcode, price_total: int, items: List[InvoiceItems] | None = None):
        self.id: int = id
        self.date: datetime = date
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.country: str = country
        self.postalCode: int = postalcode
        self.price_total: float = price_total
        self.items: List[InvoiceItems] = items if items is not None else []

    def __str__(self):
        items = [f'{item}' for item in self.items]
        return '{\n'+(f' id: {self.id},\n'
                      f' date: {self.date},\n'
                      f' address: {self.address},\n'
                      f' city: {self.city},\n'
                      f' state: {self.state},\n'
                      f' country: {self.country},\n'
                      f' postalcode: {self.postalCode},\n'
                      f' total price: {self.price_total},\n'
                      f' items: {items},\n') + '}'

    async def add_item(self, item: InvoiceItems) -> None:
        if isinstance(item, InvoiceItems):
            self.items.append(item)
        else:
            raise TypeError(f"the item argument not is type InvoiceItems, it is type {type(item)}"
                            + f"class:{__class__} in {__name__} {__file__}")

    async def add_items(self, todo_items: List[InvoiceItems]) -> None:
        if isinstance(todo_items, List):
            for item in todo_items:
                await self.add_item(item)
        else:
            raise TypeError(f"the item argument not is type InvoiceItems, it is type {type(todo_items)}"
                            + f"class:{__class__} in {__name__} {__file__}")

    async def calculate_total_price(self) -> int:

        prices_total = await asyncio.gather(*[
            item.calculate_total_item_price()
            for item in self.items
        ])
        return sum(prices_total)

    def set_price_total(self, price: float):
        if isinstance(price, int):
            self.price_total = price
        else:
            raise TypeError(f"the price argument no is type int, it is type {type(price)}" +
                            "class:{__class__} in {__name__} {__file__}")
