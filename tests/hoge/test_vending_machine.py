from vending_machine.hoge.vending_machine import VendingMachine


class TestVendingMachine:
    def test_insert(self):
        vm = VendingMachine()

        assert vm.insert(10) == 10

    def test_show_total(self):
        vm = VendingMachine()

        add_total = vm.insert(10)
        add_total = vm.insert(50)
        add_total = vm.insert(50)

        assert vm.show_total() == add_total
