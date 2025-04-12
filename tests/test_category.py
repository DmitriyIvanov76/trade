from src.category import Category

class TestCategory:
    def test_category(self, telephone_category):
        name, description, products = telephone_category
        new_category = Category(name, description, products)
        assert new_category.name == "смартфоны"
        assert new_category.description == "Смартфоны, как средство не только коммуникации"
        assert new_category.products == [("Motorola", "телефоны двухтысячных", 7500, 25),
            ("Ericsson", "телефоны двухтысячных", 10000.3, 12)]
        assert Category.category_count == 1
    # проверка Category.product_count
    def test_added_products(self,telephone_category, added_product):
        name, description, products = telephone_category
        new_category = Category(name, description, products)
        new_category.add_product(added_product)
        assert Category.product_count == len(products) + 1



