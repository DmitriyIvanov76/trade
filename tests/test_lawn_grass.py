import pytest
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone


class TestLawnGrass:
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

    def test_new_grass(self, grass_dict):
        new_grass = LawnGrass.new_product(grass_dict)
        assert new_grass.name == "football"


class TestAddedGrass:
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


class TestOutputGrass:
    # вывод информации при создании объекта
    def test_output_text(self, lawn_grass, capsys):
        name, description, price, quantity, country, germination_period, color = lawn_grass
        LawnGrass(name, description, price, quantity, country, germination_period, color)
        captured = capsys.readouterr()
        assert captured.out.strip() == "LawnGrass, Для спорт. площадок, 696, 10"
