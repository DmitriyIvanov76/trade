from unittest.mock import patch

import pytest

from src.product import Product


class TestProduct:
    @pytest.mark.parametrize(
        "name, description, price, quantity",
        [
            ("Samsung", "256GB", 50000, 5),
            ("Samsung", "256GB", 50000, 5),
            ("Samsung", "256GB", 50000, 5),
            ("Samsung", "256GB", 50000, 5),
        ],
    )
    def test_product(self, name, description, price, quantity):
        product = Product(name, description, price, quantity)

        assert product.name == "Samsung"
        assert product.description == "256GB"
        assert product.price == 50000
        assert product.quantity == 5


# тестирование класс метода new_product
class TestProductClassMethod:
    # тест с одним аргументом
    def test_new_product(self, new_product_test):
        new_product = Product.new_product(new_product_test)
        assert new_product.name == "Sony"
        assert new_product.description == "64mb, Серый цвет, 3MP камера"
        assert new_product.price == 80000.0
        assert new_product.quantity == 11

    # тест с двумя аргументами
    def test_new_product_two_arguments(self, new_product_test, product_test_old_list):
        new_product = Product.new_product(new_product_test, product_test_old_list)
        assert new_product.name == "Sony"
        assert new_product.description == "64mb, Серый цвет, 3MP камера"
        assert new_product.price == 210000.0
        assert new_product.quantity == 20


class TestProductGetter:
    def test_get_product_info(self, new_product_test):
        new_product = Product.new_product(new_product_test)
        assert new_product.product_info == "Sony, 80000.0 руб. Остаток: 11 шт."

    def test_get_price(self, new_product_test):
        new_product = Product.new_product(new_product_test)
        assert new_product.price == 80000.0


class TestProductSetter:
    @patch("builtins.input", side_effect="y")
    def test_price_setter(self, mock_input, new_product_test):
        new_product = Product.new_product(new_product_test)
        new_product.price = 9000
        assert new_product.price == 9000

    @patch("builtins.input", side_effect="y")
    def test_zero_price_setter(self, mock_input, new_product_test):
        new_product = Product.new_product(new_product_test)
        new_product.price = 0
        assert new_product.price == new_product.price


class TestStr:
    def test_str(self, mobile_telephone, capsys):
        Product("Samsung", "256GB", 50000, 5)
        captured = capsys.readouterr()
        assert captured.out.strip() == "Product, 256GB, 50000, 5"
