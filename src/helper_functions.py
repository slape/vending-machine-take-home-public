import typing
import json
from pprint import pprint


class VendingMachine():
    def __init__(self, items, credit=0):
        self.items = items
        self.credit = credit

    def display_credit(self):
        print(f"Credit: {self.credit}")

    def display_options(self):
        for num, item in enumerate(self.items):
            print(num, item['name'], item['price'])


def read_items() -> dict:
    with open('data/items.json') as json_file:
        items = json.load(json_file)
    return items


def select_product(selection: int) -> tuple:
    """
    As a vendor
    I want customers to select products
    So that I can give them products

    There are three products:
    cola, chips, and candy.
    When the respective button is pressed,
    the product is dispensed and the machine displays THANK YOU.
    """
