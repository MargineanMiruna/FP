from entities.address import Address


class Student:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'name: {self.name}, address: {self.address}'

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name
