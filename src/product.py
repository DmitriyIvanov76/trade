from typing import Union

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    name: int
    description: str
    price: Union[float | int]
    quantity: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    # просмотр товара
    @property
    def product_info(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    # принимает на вход словарь с параметрами, возвращает созданный объект
    # второй параметр список существующих товаров, при совпадении изменяются параметры существующего товара
    @classmethod
    def new_product(cls, new_product_dict: dict, old_product_list: list = None):

        name = new_product_dict.get("name")
        description = new_product_dict.get("description")
        price = new_product_dict.get("price")
        quantity = new_product_dict.get("quantity")

        if old_product_list is not None and any(i[0] == name for i in old_product_list):
            new_price = max(price, max(i[-2] for i in old_product_list if i[0] == name))
            new_quantity = quantity + sum(i[-1] for i in old_product_list if i[0] == name)

            return cls(name, description, new_price, new_quantity)

        return cls(name, description, price, quantity)

    # обращение к приватной цене
    @property
    def price(self):
        return self.__price

    # изменение приватной цены
    @price.setter
    def price(self, price: [float | int]):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if price < self.price:
                options = input("Подтвердите снижение цены, YES(Y) или NO(N): ").lower()
                if options == "y":
                    self.__price = price
                else:
                    self.price = self.price

    # метод складывания атрибутов объекта
    def __add__(self, other):
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


if __name__ == "__main__":
    di = {"name": "Sony", "description": "64mb, Серый цвет, 3MP камера", "price": 80000.0, "quantity": 11}
    a = Product.new_product(di)
