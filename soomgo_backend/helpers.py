from luhn import verify


class CreditCard:
    card_id = None  # 카드 번호
    name = None
    balance = 0
    limit = 0
    is_valid = True

    def __init__(self, card_id, card_name, limit):
        if not verify(card_id):
            # Luhn invalid
            self.is_valid = False

        self.card_id = card_id
        self.name = card_name
        self.limit = int(limit)

    def charge(self, amount: str):
        if not verify(amount):
            return  # Luhn invalid
        if self.limit > self.balance + int(amount):
            return  # 한도액 초과
        self.balance += int(amount)

    def credit(self, amount):
        if not verify(amount):
            return  # Luhn invalid
        self.balance -= int(amount)
