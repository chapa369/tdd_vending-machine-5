"""sample"""


class VendingMachine:
    """
    Vending Machine class
    """

    def __init__(self):
        self.total = 0

    def insert(self, add_money) -> str:
        """insert money"""
        self.total += add_money
        return self.total
