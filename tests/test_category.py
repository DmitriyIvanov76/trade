
from src.category import Category
from src.product import Product


class TestCategory:
    def test_category(self, telephone_category):
        name, description, products = telephone_category
        new_category = Category(name, description, products)
        assert new_category.name == "смартфоны"
        assert new_category.description == "Смартфоны, как средство не только коммуникации"
        assert Category.category_count == 3

    # проверка Category.product_count
    def test_added_products(self, telephone_category, product_instance):
        name, description, products = telephone_category
        new_category = Category(name, description, products)
        new_category.add_product(product_instance)
        assert Category.product_count == 8

    # проверка вывода str
    def test_str(self, capsys):
        product1 = Product("Motorola", "телефоны двухтысячных", 7500.0, 25)
        product2 = Product("Ericsson", "телефоны двухтысячных", 10000.3, 12)
        new_category = Category("смартфоны", "Смартфоны, как средство не только коммуникации", [product1, product2])
        print(str(new_category))
        captured = capsys.readouterr()
        output_text = (
            "Product, телефоны двухтысячных, 7500.0, 25\n"
            "Product, телефоны двухтысячных, 10000.3, 12\n"
            "смартфоны, количество продуктов: 37 шт."
        )
        assert captured.out.strip() == output_text


class TestMiddlePrice:
    def test_middle_price(self, telephone_category):
        name, description, products = telephone_category
        new_devices = Category(name, description, products)
        assert new_devices.middle_price() == 8750.15

    def test_middle_price_empty_product(self, telephone_category_zero_list):
        name, description, products = telephone_category_zero_list
        new_devices = Category(name, description, products)
        assert new_devices.middle_price() == 0
