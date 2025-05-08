import pytest

from src.product import Product


# для тестирования product.py
@pytest.fixture
def mobile_telephone():
    return Product(name="Samsung", description="256GB", price=50000, quantity=5)


# тест для product.py (продукт)
@pytest.fixture
def name_product():
    return "Samsung", "256GB", 50000, 5


# для тестирования category.py
@pytest.fixture
def telephone_category():
    name, description = ("смартфоны", "Смартфоны, как средство не только коммуникации")
    moto = Product("Motorola", "телефоны двухтысячных", 7500, 25)
    ericsson = Product("Ericsson", "телефоны двухтысячных", 10000.3, 12)
    products = [moto, ericsson]
    return name, description, products


# тест пустого списка category.py (middle_price)
@pytest.fixture
def telephone_category_zero_list():
    name, description, products = ("смартфоны", "Смартфоны, как средство не только коммуникации", [])
    return name, description, products


# для теста добавления продукта в category.py(add.product)
@pytest.fixture
def added_product():
    return [("Iphone 15", "512GB, Gray space", 210000.0, 8)]


@pytest.fixture
def new_product_test():
    return {"name": "Sony", "description": "64mb, Серый цвет, 3MP камера", "price": 80000.0, "quantity": 11}


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
    name, description, price, quantity = "Sony", "64mb, Серый цвет, 3MP камера", 210000.0, 20
    return name, description, price, quantity


# экземпляр класса Product для теста add_product
@pytest.fixture
def product_instance():
    new_product = Product("Nokia", "N95", 17000.0, 7)
    return new_product


# тестирование smartphone.py
@pytest.fixture
def smartphone():
    name, description, price, quantity, efficiency, model, memory, color = (
        "samsung",
        "android9",
        12000,
        10,
        "279",
        "s7",
        "256",
        "grey",
    )
    return name, description, price, quantity, efficiency, model, memory, color


# тестирование lawn_grass.py
@pytest.fixture
def lawn_grass():
    name, description, price, quantity, country, germination_period, color = (
        "футбол",
        "Для спорт. площадок",
        696,
        10,
        "Rus",
        "mouth",
        "green",
    )
    return name, description, price, quantity, country, germination_period, color


# словарь для тестирования smartphone.py
@pytest.fixture
def smartphones():
    device = {
        "name": "Iphone 14",
        "description": "for India",
        "price": 47600,
        "quantity": 18,
        "efficiency": "6‑core CPU",
        "model": "Pro Max",
        "memory": "256Gb",
        "color": "black",
    }
    return device


@pytest.fixture
def grass_dict():
    grass = {
        "name": "football",
        "description": "football pitch",
        "price": 720,
        "quantity": 10,
        "country": "Belgium",
        "germination_period": "1 mouth",
        "color": "green",
    }
    return grass
