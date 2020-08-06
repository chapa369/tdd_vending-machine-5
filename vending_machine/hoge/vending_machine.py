"""sample"""


class VendingMachine:
    """
    Vending Machine class
    """

    def __init__(self):
        self.add_total = 0
        self.price_total = 0

    def insert(self, add_money) -> int:
        """insert money"""
        self.add_total += add_money
        return self.add_total

    def show_total(self) -> int:
        """show total money"""
        return self.add_total

    # def refund(self) -> int:
    #     """refund money"""
    #     refund_total = self.add_total - self.price_total
    #     return refund_total
