from vending_machine.hoge.vending_machine import VendingMachine
import pytest


class TestVendingMachine:
    @pytest.mark.parametrize("coin,added_to_total", [(10, 10), (20, 0)])
    def test_insert(self, coin, added_to_total):
        vm = VendingMachine()
        # 10円玉、50円玉、100円玉、500円玉、1000円札を１つずつ投入できる。
        assert vm.insert(coin) == added_to_total
        # assert vm.insert(coin)

    def test_show_total(self):
        vm = VendingMachine()
        insert_coin = [10, 20, 50, 50]
        total_test = 0
        for coin in insert_coin:
            total_test += vm.insert(coin)
        assert vm.show_total() == total_test

    def test_refund(self):
        vm = VendingMachine()
        insert_coin = [10, 20, 50, 50]
        total_test = 0
        for coin in insert_coin:
            total_test += vm.insert(coin)
        assert vm.show_total() == total_test

    def test_buy(self):
        pass
