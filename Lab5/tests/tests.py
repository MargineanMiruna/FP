from modelle.modelle import GekochterGericht, Kunde, Bestellung
from repository.repo import CookedDishRepo, DrinkRepo, CustomerRepo
from controller.controller import Controller


def test_add_ger():
    repo = CookedDishRepo('test_dishes.data')
    dish = GekochterGericht(1, 'Bread', 70, 5, 1)
    repo.add(dish)
    repo.load()
    assert repo.dishes[-1] == dish


def test_search_name():
    ctr = Controller(CustomerRepo('customers.data'))
    assert ctr.search('miru', 9) == [ctr.repo.customers[0]]


def test_search_adr():
    ctr = Controller(CustomerRepo('customers.data'))
    assert ctr.search('rozelor', 10) == [ctr.repo.customers[1]]


def test_update_cust():
    repo1 = CustomerRepo('customers.data')
    cust = repo1.customers
    repo2 = CustomerRepo('test_customers.data')
    repo2.save(cust)
    id = 4
    name = 'Olivia Marcus'
    for c in cust:
        if c.id == id:
            i = cust.index(c)
            break
    cust[i] = Kunde(id, name, cust[i].adr)
    repo2.save(cust)
    repo2.load()
    assert repo2.customers[i].name == name


def test_rech():
    bill = Bestellung(1, 3, [1, 4, 9], [1, 5])
    bill.get_ger(CookedDishRepo('dishes.data').dishes)
    bill.get_get(DrinkRepo('drinks.data').drinks)
    bill.add_kosten()
    rech = """
Order nr. 1
Customer 3
French Fries - 12.5
Pizza - 40.0
Sushi - 36.8
Water - 6.0
Coffee - 13.0
Total: 108.3"""
    print(rech)
    assert bill.anz_rechnung() == rech



