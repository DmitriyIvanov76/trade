class IteratorCategory:

    def __init__(self, category):
        self.category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.category.products):
            product = self.category.products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration
