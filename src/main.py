import helper_functions


def main():
    items = helper_functions.read_items()
    vend = helper_functions.VendingMachine(items)

    vend.display_credit()
    vend.display_options()


if __name__ == "__main__":
    main()
