from helper_functions import *

items = read_items()


def select_product_test():
    """Test to see if a selected producet is correctly despensed."""
    selection = select_product(items, 1)
    assert selection == "cola", "Failed"
    selection = select_product(2)
    assert selection == "chips", "Failed"
    selection = select_product(3)
    assert selection == "candy", "Failed"
    selection = select_product(4)
    assert selection == "invalid selection", "Failed"
    selection = select_product("coke")
    assert selection == "invalid selection", "Failed"
    selection = select_product("asdfas")
    assert selection == "invalid selection", "Failed"
    selection = select_product("234")
    assert selection == "invalid selection", "Failed"
    selection = select_product("@#$")
    assert selection == "invalid selection", "Failed"
