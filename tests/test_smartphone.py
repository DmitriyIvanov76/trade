from src.smartphone import Smartphone


class TestSmartphone:
    def test_get_product(self, smartphone):
        name, description, price, quantity, efficiency, model, memory, color = smartphone
        new_smart = Smartphone(name, description, price, quantity, efficiency, model, memory, color)
        assert new_smart.name == "samsung"
        assert new_smart.description == "android9"
        assert new_smart.price == 12000
        assert new_smart.quantity == 10
        assert new_smart.efficiency == "279"
        assert new_smart.model == "s7"
        assert new_smart.memory == "256"
        assert new_smart.color == "grey"
