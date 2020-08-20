from vending_machine.hoge.vending_machine import VendingMachine


class TestVendingMachine:
    def test_insert(self):
        vm = VendingMachine()
        # 10円玉、50円玉、100円玉、500円玉、1000円札を１つずつ投入できる。
        assert vm.insert(10) == 10
        assert vm.insert(20) == 0

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

