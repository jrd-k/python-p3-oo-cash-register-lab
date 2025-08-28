class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self._items = []
        self.last_transaction = 0

    @property
    def items(self):
        return self._items

    def add_item(self, title, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount

        for _ in range(quantity):
            self._items.append(title)

        self.last_transaction = transaction_amount

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total = int(self.total - discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0
