import helper_functions


def main():
    items = helper_functions.read_items()
    vend = helper_functions.VendingMachine(items)
    vend.display_credit()
    vend.display_options()
    # ask for input or quit
    # check input
    # select product
    # accept coins
    # pay for product
    # make change


if __name__ == "__main__":
    main()
