from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def new_product(self, new_product_dict, old_product_list):
        pass
