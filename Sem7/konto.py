class Konto:
    def __init__(self, nr: int, admin: str, betrag: int = 0):
        self.nr = nr
        self.betrag = betrag
        self.admin = admin

    def einzahlen(self, sum):
        self.betrag += sum

    def auszahlen(self, sum):
        self.betrag -= sum