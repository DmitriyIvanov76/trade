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

    # добавление приватного параметра
    def add_product(self, prod):
        if isinstance(prod, Product):
            self.__products.append(prod)
        else:
            raise TypeError(f'{prod} должен быть экземпляром класса {Product}')

    # обращение к приватному параметру
    @property
    def products(self):
        return self.__products


# if __name__ == '__main__':

