def test_category(telephone_category):
    assert telephone_category.name == "смартфоны"
    assert telephone_category.description == "Смартфоны, как средство не только коммуникации"
    assert [
        (product.name, product.description, product.price, product.quantity) for product in telephone_category.products
    ] == [("Motorola", "телефоны двухтысячных", 7500, 25), ("Ericsson", "телефоны двухтысячных", 10000.3, 12)]
