from MenuItem import MenuItem


class MenuManager:
    def __init__(self):
        self.menu_items: dict[str, MenuItem] = {}

    def add_menu_item(self, menu_item: MenuItem) -> bool:
        if menu_item.item_code in self.menu_items:
            print(f"\nItem: {menu_item.name} already avilable in Menu!!!\n")
            return False
        self.menu_items[menu_item.item_code] = menu_item
        print(f"\nItem: {menu_item.name} added to Menu!!!\n")
        return True

    def remove_menu_item(self, item_code: str):
        if item_code not in self.menu_items:
            print(f'\nItem: {item_code} not in Menu!!!\n')
            return False
        menu_item = self.menu_items[item_code]
        del self.menu_items[item_code]
        print(f"\nItem {menu_item.name} successfully removed from Menu!!!\n")
        return True

    def show_menu(self, category: str = None):
        ...

    def update_item_price(self, item_code: str, new_price: float) -> bool:
        if item_code not in self.menu_items:
            print(f"Item with code-{item_code} not available in Menu!!!")
            return False
        menu_item: MenuItem = self.menu_items[item_code]
        menu_item.set_price(new_price)
        print(f"\nPrice {new_price} for Item {menu_item.name} is"
              "successfully updated!!!\n")
        return True







