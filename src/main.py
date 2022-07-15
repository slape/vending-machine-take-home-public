from helper_functions import *


def main():
    items = read_items()
    vend = VendingMachine(items)
    vend.display_credit()
    vend.display_options()
    # ask for input or quit
    choice = input("Make a selection: ")
    # check input
    # needs input validation
    # select product
    select_product(items, int(choice))
    # accept coins
    # pay for product
    # make change


if __name__ == "__main__":
    main()
