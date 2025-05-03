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

    def remove_menu_item():
        ...

    def list_menu():
        ...

    def update_item_price():
        ...


