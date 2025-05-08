from itertools import product

from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    def __str__(self):
        total_product = sum(i.quantity for i in self.products)
        return f"{self.name}, количество продуктов: {total_product} шт."

    # добавление приватного параметра
    def add_product(self, prod):
        if isinstance(prod, Product):
            self.__products.append(prod)
        else:
            raise TypeError(f"{prod} должен быть экземпляром класса Product")

    # обращение к приватному параметру
    @property
    def products(self):
        return self.__products

    # метод подсчёта среднего ценника всех товаров
    def middle_price(self):
        try:
            result = sum(products.price for products in self.products) / len(self.products)
            return result
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    tel = [
        ("Motorola", "телефоны двухтысячных", 7500, 25),
        ("Ericsson", "телефоны двухтысячных", 10000.3, 12),
    ]
    empty_list = []
    di = {"name": "Sony", "description": "64mb, Серый цвет, 3MP камера", "price": 80000.0, "quantity": 11}
    d2 = {"name": "Sony", "description": "64mb, Серый цвет, 3MP камера", "price": 2000.0, "quantity": 11}

    b = Product.new_product(di)
    v = Product.new_product(d2)

    a = Category("смартфоны", "Смартфоны, как средство не только коммуникации", [b, v])

    print(a.products)
