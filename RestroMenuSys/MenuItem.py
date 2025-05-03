class MenuItem:
    def __init__(self, item_code: str, name: str, category: str):
        self.item_code: str = item_code
        self.name: str = name
        self.category: str = category
        self.__price: float = 0

        def set_price(self, price: float):
            self.__price = price

        def get_price(self):
            return self.__price

