from consolemenu import *
from consolemenu.items import *

menu = ConsoleMenu("Spotipy", "please enter:")

menu_item = MenuItem("Menu item")

function_item = FunctionItem("Call a Python function", input, ["enter an input"])

commend_item = CommandItem("Run a console command", "touch hello.txt")

selection_menu = SelectionMenu(["item1", "item2", "item3"])

submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(commend_item)
menu.append_item(submenu_item)

menu.show()