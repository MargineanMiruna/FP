from controller.controller import Controller
from modelle.modelle import GekochterGericht, Getrank, Kunde, Bestellung
from repository.repo import DataRepo, CookedDishRepo, DrinkRepo, CustomerRepo


class Console:
    def __init__(self, opt: int, ctr: Controller):
        self.opt = opt
        self.ctr = ctr

    def run(self):
        if self.opt == 1:
            print(self.ctr.repo.read_file())

        if self.opt == 2:
            print('What do you want to add?')
            typ = int(input('1 - Dish\n2 - Drink\n'))
            if typ == 1:
                repo1 = CookedDishRepo('dishes.data')
                dishes = repo1.dishes
                ger = input('Name of new dish: ')
                portgr = int(input('Quantity: '))
                preis = float(input('Price: '))
                zeit = int(input('Preparation time: '))
                new_ger = GekochterGericht(dishes[-1].id + 1, ger, portgr, preis, zeit)
                dishes.append(new_ger)
                repo1.save(dishes)
            else:
                repo2 = DrinkRepo('drinks.data')
                drinks = repo2.drinks
                get = input('Name of new drink: ')
                portgr = int(input('Quantity: '))
                preis = float(input('Price: '))
                alc = int(input('Alcohol content: '))
                new_get = Getrank(drinks[-1].id + 1, get, portgr, preis, alc)
                drinks.append(new_get)
                repo2.save(drinks)
            menu = self.ctr.compose_menu()
            self.ctr.repo.write_to_file(menu)

        if self.opt == 3:
            print('What do you want to update?')
            typ = int(input('1 - Dish\n2 - Drink\n'))
            if typ == 1:
                repo1 = CookedDishRepo('dishes.data')
                dishes = repo1.dishes
                id = int(input('Id of the dish you want to update: '))
                ger = input('New name of the dish: ')
                portgr = int(input('New quantity: '))
                preis = float(input('New price: '))
                zeit = int(input('New preparation time: '))
                for d in dishes:
                    if d.id == id:
                        i = dishes.index(d)
                        break
                dishes[i] = GekochterGericht(id, ger, portgr, preis, zeit)
                repo1.save(dishes)
            else:
                repo2 = DrinkRepo('drinks.data')
                drinks = repo2.drinks
                id = int(input('Id of the drink you want to update: '))
                ger = input('New name of the drink: ')
                portgr = int(input('New quantity: '))
                preis = float(input('New price: '))
                alc = int(input('New alcohol content: '))
                for d in drinks:
                    if d.id == id:
                        i = drinks.index(d)
                        break
                drinks[i] = Getrank(id, ger, portgr, preis, alc)
                repo2.save(drinks)
            menu = self.ctr.compose_menu()
            self.ctr.repo.write_to_file(menu)

        if self.opt == 4:
            print('What do you want to delete?')
            typ = int(input('1 - Dish\n2 - Drink\n'))
            if typ == 1:
                repo1 = CookedDishRepo('dishes.data')
                dishes = repo1.dishes
                id = int(input('Id of the dish you want to delete: '))
                filtered = filter(lambda x: x.id != id, dishes)
                repo1.save(list(filtered))
            else:
                repo2 = DrinkRepo('drinks.data')
                drinks = repo2.drinks
                id = int(input('Id of the drink you want to delete: '))
                filtered = filter(lambda x: x.id != id, drinks)
                repo2.save(list(filtered))
            menu = self.ctr.compose_menu()
            self.ctr.repo.write_to_file(menu)

        if self.opt == 5:
            print(self.ctr.repo.convert_to_string(self.ctr.repo.customers))

        if self.opt == 6:
            cust = self.ctr.repo.customers
            name = input('Name: ')
            adr = input('Address: ')
            self.ctr.repo.add(Kunde(cust[-1].id + 1, name, adr))

        if self.opt == 7:
            cust = self.ctr.repo.customers
            id = int(input('Id of the customer you want to update: '))
            name = input('New name: ')
            adr = input('New address: ')
            for c in cust:
                if c.id == id:
                    i = cust.index(c)
                    break
            cust[i] = Kunde(id, name, adr)
            self.ctr.repo.save(cust)

        if self.opt == 8:
            cust = self.ctr.repo.customers
            id = int(input('Id of the customer you want to delete: '))
            filtered = filter(lambda x: x.id != id, cust)
            self.ctr.repo.save(list(filtered))

        if self.opt == 9:
            search = input('Name: ')
            cust = self.ctr.search(search, self.opt)
            print(self.ctr.repo.convert_to_string(cust))

        if self.opt == 10:
            search = input('Address: ')
            cust = self.ctr.search(search, self.opt)
            print(self.ctr.repo.convert_to_string(cust))

        if self.opt == 11:
            ord = self.ctr.repo.orders
            repo1 = CustomerRepo('customers.data')
            cust = repo1.customers
            print(repo1.convert_to_string(cust))
            kid = int(input('\nId of the customer who orders: '))

            repo2 = DataRepo('menu.txt')
            print('\n' + repo2.read_file())

            repo3 = CookedDishRepo('dishes.data')
            dishes = []
            ds = input('Ids of the dishes you want to order: ')
            while ds != '':
                dishes.append(int(ds))
                ds = input()

            repo4 = DrinkRepo('drinks.data')
            drinks = []
            dr = input('Ids of the drinks you want to order: ')
            while dr != '':
                drinks.append(int(dr))
                dr = input()

            new_bes = Bestellung(self.ctr.repo.orders[-1].id + 1, kid, dishes, drinks)
            new_bes.get_ger(repo3.dishes)
            new_bes.get_get(repo4.drinks)
            new_bes.add_kosten()
            ord.append(new_bes)
            self.ctr.repo.save(ord)

        if self.opt == 12:
            ord = self.ctr.repo.orders
            print(self.ctr.repo.convert_to_string(ord))
            id = int(input('Id of the order you want to receive the bill to: '))
            print(ord[id - 1].anz_rechnung())
