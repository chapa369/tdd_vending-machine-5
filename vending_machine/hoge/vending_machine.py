"""sample"""


class VendingMachine:
    """
    Vending Machine class
    """

    def __init__(self):
        self.total = 0

    def insert(self, add_money) -> int:
        """insert money"""
        self.total += add_money
        return self.total

    def show_total(self) -> int:
        """insert money"""
        return self.total

    def refund(self) -> int:
        """insert money"""
        return self.total
