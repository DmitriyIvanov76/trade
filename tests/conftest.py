import pytest
from typing_extensions import reveal_type

from src.category import Category
from src.product import Product


# для тестирования product.py
@pytest.fixture
def mobile_telephone():
    return Product(name="Samsung", description="256GB", price=50000, quantity=5)


# для тестирования category.py
@pytest.fixture
def telephone_category():
    name, description, products = "смартфоны", "Смартфоны, как средство не только коммуникации", [
            ("Motorola", "телефоны двухтысячных", 7500, 25),
            ("Ericsson", "телефоны двухтысячных", 10000.3, 12),
        ]
    return name, description, products
# для теста добавления продукта в category.py(add.product)
@pytest.fixture
def added_product():
    return [("Iphone 15", "512GB, Gray space", 210000.0, 8)]


@pytest.fixture
def new_product_test():
    return {"name": "Sony", "description": "64mb, Серый цвет, 3MP камера", "price": 80000.0,
         "quantity": 11}

# для тестирования product.py
@pytest.fixture
def product_test_old_list():

    product1 = ("lg", "128mb, раскладушка", 180000.0, 5)
    product2 = ("Sony", "64mb, Серый цвет, 3MP камера", 210000.0, 9)
    product3 = ("Nokia", "128mb, Синий", 31000.0, 14)

    existing_list_product = [product1, product2, product3]

    return existing_list_product

# тестирование класс метода, который создает новый объект на основе словаря
@pytest.fixture
def new_product_test_result():
    name, description, price, quantity = 'Sony', '64mb, Серый цвет, 3MP камера', 210000.0, 20
    return name, description, price, quantity

