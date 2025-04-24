import pytest
from src.smartphone import Smartphone
from src.category import Category


# добавление продукта из класса
def test_added_prod(smartphone, telephone_category):
    name, description, price, quantity, efficiency, model, memory, color = smartphone
    new_smart = Smartphone(name, description, price, quantity, efficiency, model, memory, color)

    name, description, products = telephone_category
    new_telephone = Category(name, description, products)
    new_telephone.add_product(new_smart)


# добавление продукта не из класса(вызов ошибки)
def test_added_prod_error(telephone_category):
    name, description, products = telephone_category
    new_telephone = Category(name, description, products)
    new_smart = ("samsung", "android9", 12000, 10, "279", "s7", "256", "grey")

    with pytest.raises(TypeError):
        new_telephone.add_product(new_smart)
