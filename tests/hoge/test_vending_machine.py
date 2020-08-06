from vending_machine import vending_machine


class TestVendingMachine:
    vending_machine = VendingMachine()

    def test_insert(self):
        assert vending_machine.insert(10) == 10

    def test_insert(self):
        assert Huga().piyo(10) == 10



