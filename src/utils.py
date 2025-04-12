import json
import os

from src.category import Category
from src.product import Product


def reader_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, encoding="UTF-8") as file:
        content = json.load(file)
    return content


def create_object_file(data: dict) -> list:
    devices_list = []
    for category in data:
        devices = []
        for i in category["products"]:
            devices.append(Product(**i))
        category["products"] = devices
        devices_list.append(Category(**category))
    return devices_list


if __name__ == "__main__":
    raw_data = reader_json("../data/products.json")
    result = create_object_file(raw_data)

    a = Category('Smart', 'Smart как средство', result)

    print(a.get_product)