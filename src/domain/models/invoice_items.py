from .track import Track


class InvoiceItems:

    def __init__(self, id: int, track: Track, price: int, quantity: int):
        self.id: int = id
        self.track: Track = track
        self.unitPrice: int = price
        self.quantity: int = quantity

    async def calculate_total_item_price(self) -> int:
        return self.unitPrice * self.quantity

    def __str__(self):
        total: int = self.unitPrice * self.quantity
        return ('{\n' +
                f'id: {self.id},\n'
                f'track: {self.track},\n '
                f'unit price: {self.unitPrice},\n'
                f' quantity: {self.quantity},\n'
                f' total: {total}\n'
                + '}'
                )
