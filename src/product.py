class Product:
    name: int
    description: str
    price: [float | int]
    quantity: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    # просмотр товара
    @property
    def product_info(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    # принимает на вход словарь с параметрами, возвращает созданный объект
    # второй параметр словарь существующих товаров, при совпадении изменяются параметры существующего товара
    @classmethod
    def new_product_dict(cls, new_product_dict: dict, old_product_dict: dict = None):

        name, description, price, quantity = [i for i in new_product_dict.values()]

        if old_product_dict is not None and name == old_product_dict["name"]:
            new_price = max(price, old_product_dict["price"])
            new_quantity = quantity + old_product_dict["quantity"]

            return cls(name, description, new_price, new_quantity)

        return cls(name, description, price, quantity)

    # принимает на вход словарь с параметрами, возвращает созданный объект
    # второй параметр список существующих товаров, при совпадении изменяются параметры существующего товара
    @classmethod
    def new_product(cls, new_product_dict: dict, old_product_list: list = None):

        name, description, price, quantity = [i for i in new_product_dict.values()]

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
        return self.price * self.quantity + other.price * other.quantity

# if __name__ == '__main__':
