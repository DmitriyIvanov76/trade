from src.product import Product


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency="unknown", model="unknown", memory=0, color="unknown"
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        print(repr(self))

    # дополнен класс метод родительского класса для создания объекта
    @classmethod
    def new_product(cls, new_product_dictionary: dict, old_product_dict: dict = None):
        product_inst = super().new_product(new_product_dictionary, old_product_dict)

        efficiency = new_product_dictionary.get("efficiency", "unknown")
        model = new_product_dictionary.get("model", "unknown")
        memory = new_product_dictionary.get("memory", 0)
        color = new_product_dictionary.get("color", "unknown")

        return cls(
            product_inst.name,
            product_inst.description,
            product_inst.price,
            product_inst.quantity,
            efficiency,
            model,
            memory,
            color,
        )
