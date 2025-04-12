import pytest
from src.product import Product

@pytest.mark.parametrize(
    'name, description, price, quantity',
    [
        ('Samsung', '256GB', 50000, 5),
        ('Samsung', '256GB', 50000, 5),
        ('Samsung', '256GB', 50000, 5),
        ('Samsung', '256GB', 50000, 5)
    ]
)


def test_product(name, description, price, quantity):
   product = Product(name, description, price, quantity)

   assert product.name == 'Samsung'
   assert product.description == '256GB'
   assert product.price == 50000
   assert product.quantity == 5