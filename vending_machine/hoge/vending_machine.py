"""sample"""


price = {"コーラ": 120}


class VendingMachine:
    """
    Vending Machine class
    """

    def __init__(self):
        self.add_total = 0  # 投入金額の合計
        self.revenue = 0  # 売り上げ金額
        self.storage = {"コーラ": 5}
        # self.price_total = 0

    def insert(self, add_money) -> int:
        """insert money"""
        if add_money in [10, 50, 100, 500, 100, 1000]:
            self.add_total += add_money
            return add_money
        else:
            print(add_money)
            return 0

    def show_total(self) -> int:
        """show total money"""
        return self.add_total

    def refund(self) -> int:
        """refund money"""
        refund_total = self.add_total
        self.add_total = 0
        return refund_total

    # 全商品の在庫確認
    def show_storage(self):
        all_storage = []
        for beverage in self.storage.keys():
            all_storage.append(
                {"name": beverage, "price": price[beverage], "store": self.storage[beverage]}
            )
        return all_storage

    def buy(self, beverage):
        if beverage == "コーラ":
            if self.add_total >= price["コーラ"] and self.storage["コーラ"] >= 1:
                # 金額が減る
                self.add_total -= price["コーラ"]
                # 在庫が減る
                self.storage["コーラ"] -= 1
                # 売り上げ↑
                self.revenue += price["コーラ"]
            else:
                pass

