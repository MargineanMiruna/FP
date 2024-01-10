import functools


class Identifizierbar:
    def __init__(self, id: int):
        self.id = id


class Gericht(Identifizierbar):
    def __init__(self, id: int, ger: str, portgr: int, preis: float):
        Identifizierbar.__init__(self, id)
        self.ger = ger
        self.portgr = portgr
        self.preis = preis

    def __str__(self):
        return f'{self.id}, {self.ger}, {self.portgr}, {self.preis}'


class GekochterGericht(Gericht):
    def __init__(self, id: int, ger: str, portgr: int, preis: float, zeit: int):
        Gericht.__init__(self, id, ger, portgr, preis)
        self.zeit = zeit

    def __str__(self):
        return f'{self.id}, {self.ger}, {self.portgr} g, {self.preis} lei, {self.zeit} min'

    def __eq__(self, other):
        return self.id == other.id and self.ger == other.ger and self.portgr == other.portgr and self.preis == other.preis and self.zeit == other.zeit


class Getrank(Gericht):
    def __init__(self, id: int, ger: str, portgr: int, preis: float, alc: int):
        Gericht.__init__(self, id, ger, portgr, preis)
        self. alc = alc

    def __str__(self):
        return f'{self.id}, {self.ger}, {self.portgr} ml, {self.preis} lei, {self.alc}% alc'


class Kunde(Identifizierbar):
    def __init__(self, id: int, name: str, adr: str):
        Identifizierbar.__init__(self, id)
        self.name = name
        self.adr = adr

    def __str__(self):
        return f'{self.id}, {self.name}, {self.adr}'


class Bestellung(Identifizierbar):
    def __init__(self, id: int, kid: int, gerichte: list, getranke: list, kosten: float = 0):
        Identifizierbar.__init__(self, id)
        self.kid = kid
        self.gerichte = gerichte
        self.getranke = getranke
        self.kosten = 0

    def __str__(self):
        return f'Id: {self.id}, Customer-ID: {self.kid}, Dishes: {[ger.ger for ger in self.gerichte]}, Drinks: {[get.ger for get in self.getranke]}, Total: {self.kosten}'

    def get_ger(self, l):
        for obj in l:
            for i in range(len(self.gerichte)):
                if obj.id is self.gerichte[i]:
                    self.gerichte[i] = obj

    def get_get(self, l):
        for obj in l:
            for i in range(len(self.getranke)):
                if obj.id is self.getranke[i]:
                    self.getranke[i] = obj

    def add_kosten(self):
        tot = [0] + self.gerichte + self.getranke
        self.kosten = functools.reduce(lambda a, b: a + b.preis, tot)

    def __rechnung(self):
        rech = '\n'
        rech = rech + f'Order nr. {self.id}\n'
        rech = rech + f'Customer {self.kid}\n'
        for ger in self.gerichte:
            rech += f'{ger.ger} - {ger.preis}\n'
        for get in self.getranke:
            rech += f'{get.ger} - {get.preis}\n'
        rech = rech + f'Total: {self.kosten}'
        return rech

    def anz_rechnung(self):
        rech = self.__rechnung()
        return rech
