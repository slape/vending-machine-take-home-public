from src.helper_functions import select_product


def select_product_test():
    """Test to see if a selected producet is correctly despensed."""
    selection = select_product(1)
    assert selection == ["coke", "THANK YOU"], "Failed"
    selection = select_product(2)
    assert selection == ["chips", "THANK YOU"], "Failed"
    selection = select_product(3)
    assert selection == ["candy", "THANK YOU"], "Failed"
    selection = select_product(4)
    assert selection == ["invalid selection", "Try Again"], "Failed"
    selection = select_product("coke")
    assert selection == ["invalid selection", "Try Again"], "Failed"
    selection = select_product("asdfas")
    assert selection == ["invalid selection", "Try Again"], "Failed"
    selection = select_product("234")
    assert selection == ["invalid selection", "Try Again"], "Failed"
    selection = select_product("@#$")
    assert selection == ["invalid selection", "Try Again"], "Failed"
