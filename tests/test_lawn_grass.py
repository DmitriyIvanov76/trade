import pytest
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone


class TestSmartphone:
    def test_lawn_grass(self, lawn_grass):
        name, description, price, quantity, country, germination_period, color = lawn_grass
        sport_lawn = LawnGrass(name, description, price, quantity, country, germination_period, color)
        assert sport_lawn.name == "футбол"
        assert sport_lawn.description == "Для спорт. площадок"
        assert sport_lawn.price == 696
        assert sport_lawn.quantity == 10
        assert sport_lawn.country == "Rus"
        assert sport_lawn.germination_period == "mouth"
        assert sport_lawn.color == "green"


class TestAddedSmartphone:
    # сложение объектов двух разных классов, наследованных от одного родительского
    def test_addition_different_classes(self, smartphone, lawn_grass):
        name, description, price, quantity, efficiency, model, memory, color = smartphone
        smart = Smartphone(name, description, price, quantity, efficiency, model, memory, color)

        name, description, price, quantity, country, germination_period, color = lawn_grass
        lawn = LawnGrass(name, description, price, quantity, country, germination_period, color)

        with pytest.raises(TypeError):
            smart + lawn

    # сложение объектов двух одинаковых классов
    def test_addition_identical_classes(self, lawn_grass):
        name, description, price, quantity, country, germination_period, color = lawn_grass
        lawn = LawnGrass(name, description, price, quantity, country, germination_period, color)
        second_lawn = LawnGrass(name, description, price, quantity, country, germination_period, color)

        assert lawn + second_lawn == 13920
