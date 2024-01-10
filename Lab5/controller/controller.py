from repository.repo import CookedDishRepo, DrinkRepo


class Controller:
    def __init__(self, repo):
        self.repo = repo

    @staticmethod
    def compose_menu():
        menu = 'Dishes:\n'
        repo1 = CookedDishRepo('dishes.data')
        dishes = repo1.dishes
        menu += repo1.convert_to_string(dishes)

        menu += '\nDrinks:\n'
        repo2 = DrinkRepo('drinks.data')
        drinks = repo2.drinks
        menu += repo2.convert_to_string(drinks)

        return menu

    def search(self, s, opt):
        if opt == 9:
            filtered = filter(lambda x: s.lower() in x.name.lower(), self.repo.customers)
        else:
            filtered = filter(lambda x: s.lower() in x.adr.lower(), self.repo.customers)
        return list(filtered)
