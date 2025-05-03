from MenuManager import MenuManager
from MenuItem import MenuItem

# class Main:
#     def __init__(self):
#         self.menu_manager: MenuManager = MenuManager()




# if __name__ == "__Main__":
#     main: Main = Main()

menu_manager: MenuManager = MenuManager()
menu_manager.show_menu()

item1: MenuItem = MenuItem('101', 'Mix Berries', 'Ice Cream')
item1.set_price(150)

item2: MenuItem = MenuItem('102', 'Blueberry', 'Ice Cream')
item2.set_price(140)
menu_manager.add_menu_item(item1)
menu_manager.add_menu_item(item2)

# show menu
menu_manager.show_menu()

# update price
menu_manager.update_item_price('101', 200)
menu_manager.show_menu()

# remove item
menu_manager.remove_menu_item('102')
menu_manager.show_menu()


