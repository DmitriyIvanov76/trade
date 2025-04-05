import pytest

from src.category import Category
from src.product import Product


# для тестирования product.py
@pytest.fixture
def mobile_telephone():
    return Product(name="Samsung", description="256GB", price=50000, quantity=5)


# для тестирования category.py
@pytest.fixture
def telephone_category():
    return Category(
        name="смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[
            Product("Motorola", "телефоны двухтысячных", 7500, 25),
            Product("Ericsson", "телефоны двухтысячных", 10000.3, 12),
        ],
    )
