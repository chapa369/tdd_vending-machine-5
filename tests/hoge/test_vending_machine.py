from vending_machine.hoge.vending_machine import VendingMachine


class TestVendingMachine:
    def test_insert(self):
        vending_machine = VendingMachine()
        assert vending_machine.insert(10) == 10

    # def test_insert(self):
    #   assert Huga().piyo(10) == 10

