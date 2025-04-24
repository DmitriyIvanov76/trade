from src.iterator import IteratorCategory
from src.category import Category
import pytest


def test_iterator(telephone_category):
    name, description, products = telephone_category
    new_category = Category(name, description, products)
    iterator = IteratorCategory(new_category)

    assert next(iterator) == products[0]
    assert next(iterator) == products[1]

    with pytest.raises(StopIteration):
        next(iterator)
