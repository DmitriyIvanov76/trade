from src.category import Category

def test_category(telephone_category):
    assert telephone_category.name == "смартфоны"
    assert telephone_category.description == "Смартфоны, как средство не только коммуникации"
    assert [
        (product.name, product.description, product.price, product.quantity) for product in telephone_category.products
    ] == [("Motorola", "телефоны двухтысячных", 7500, 25), ("Ericsson", "телефоны двухтысячных", 10000.3, 12)]

def test_get_product():
    assert Category.products == '<property object at 0x00000196B2DBCF40>'