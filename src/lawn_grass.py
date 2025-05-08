from src.product import Product


class LawnGrass(Product):

    def __init__(
        self, name, description, price, quantity, country="unknown", germination_period="unknown", color="unknown"
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    # дополнен класс метод родительского класса для создания объекта
    @classmethod
    def new_product(cls, new_product_dictionary: dict, old_product_dict: dict = None):
        product_inst = super().new_product(new_product_dictionary, old_product_dict)

        country = new_product_dictionary.get("country", "unknown")
        germination_period = new_product_dictionary.get("germination_period", "unknown")
        color = new_product_dictionary.get("color", "unknown")

        return cls(
            product_inst.name,
            product_inst.description,
            product_inst.price,
            product_inst.quantity,
            country,
            germination_period,
            color,
        )



if __name__ == "__main__":
    a = LawnGrass.new_product(
        {
            "name": "a",
            "description": "b",
            "price": 1,
            "quantity": 2,
            "country": "c",
            "germination_period": "d",
            "color": "e",
        }
    )
