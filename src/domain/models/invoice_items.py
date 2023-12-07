from .track import Track


class InvoiceItems:

    def __init__(self, id, track, price, quantity):
        self.id: int = id
        self.track: Track = track
        self.unitPrice: int = price
        self.quantity: int = quantity

    async def calculate_total_item_price(self) -> int:
        return self.unitPrice * self.quantity
