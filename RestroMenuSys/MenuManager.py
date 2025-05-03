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

    def list_menu():
        ...

    def update_item_price():
        ...


