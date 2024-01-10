class Address:
    def __init__(self, street: str, nr: int):
        self.street = street
        self.nr = nr

    def __str__(self):
        return f'street: {self.street}, number: {self.nr}'

