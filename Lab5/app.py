from ui.console import Console
from controller.controller import Controller
from repository.repo import DataRepo, CustomerRepo, OrderRepo
from tests.tests import *


def menu():
    return """
    1 - Show Menu
    2 - Add to Menu
    3 - Update Menu
    4 - Delete from Menu

    5 - Show Customers
    6 - Add Customer
    7 - Update Customer
    8 - Delete from Customers
    9 - Search Customer after Name
    10 - Search Customer after Address

    11 - New Order
    12 - Bill

    13 - Exit
    """


def main():
    while True:
        print(menu())
        opt = int(input('Option: '))

        if opt <= 4:
            c = Console(opt, Controller(DataRepo('menu.txt')))
            c.run()
        elif opt <= 10:
            c = Console(opt, Controller(CustomerRepo('customers.data')))
            c.run()
        elif opt < 13:
            c = Console(opt, Controller(OrderRepo('orders.data')))
            c.run()
        else:
            break


test_add_ger()
test_search_name()
test_search_adr()
test_update_cust()
test_rech()
test_save_convert()
test_load_convert()
main()
