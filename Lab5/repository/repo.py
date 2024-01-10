import pickle
import functools
import os
from modelle.modelle import GekochterGericht, Getrank, Kunde, Bestellung


class DataRepo:
    def __init__(self, file: str):
        self.file = file
        self.list = []

    def add(self, el):
        self.list.append(el)
        self.save(self.list)

    def save(self, li):
        f = open(self.file, 'wb')
        pickle.dump(li, f)
        f.close()

    def load(self):
        f = open(self.file, 'rb')
        self.list = pickle.load(f)
        f.close()

    def read_file(self):
        f = open(self.file, 'r')
        text = f.read()
        f.close()
        return text

    def write_to_file(self, text):
        f = open(self.file, 'w')
        f.write(text)
        f.close()

    @staticmethod
    def convert_to_string(l):
        pass

    @staticmethod
    def convert_from_string(s):
        pass


class CookedDishRepo(DataRepo):
    def __init__(self, file: str):
        DataRepo.__init__(self, file)
        self.dishes = []
        if os.path.exists(self.file):
            self.load()
        self.dishes = self.list

    @staticmethod
    def convert_to_string(ds: list):
        return functools.reduce(lambda a, b: a + b, map(lambda x: str(x) + '\n', ds))

    @staticmethod
    def convert_from_string(s: str):
        lines = s.split('\n')
        lines = [x.split(', ') for x in lines]
        lines.pop(-1)
        lines = list(map(lambda x: GekochterGericht(int(x[0]), x[1], int(x[2]), float(x[3]), int(x[4])), lines))
        return lines


class DrinkRepo(DataRepo):
    def __init__(self, file: str):
        DataRepo.__init__(self, file)
        self.drinks = []
        if os.path.exists(self.file):
            self.load()
        self.drinks = self.list

    @staticmethod
    def convert_to_string(dr: list):
        return functools.reduce(lambda a, b: a + b, map(lambda x: str(x) + '\n', dr))

    @staticmethod
    def convert_from_string(s: str):
        lines = s.split('\n')
        lines = [x.split(', ') for x in lines]
        lines.pop(-1)
        lines = list(map(lambda x: Getrank(int(x[0]), x[1], int(x[2]), float(x[3]), int(x[4])), lines))
        return lines


class CustomerRepo(DataRepo):
    def __init__(self, file: str):
        DataRepo.__init__(self, file)
        self.customers = []
        if os.path.exists(self.file):
            self.load()
        self.customers = self.list

    @staticmethod
    def convert_to_string(cust: list):
        return functools.reduce(lambda a, b: a + b, map(lambda x: str(x) + '\n', cust))

    @staticmethod
    def convert_from_string(s: str):
        lines = s.split('\n')
        lines = [x.split(', ') for x in lines]
        lines.pop(-1)
        lines = list(map(lambda x: Kunde(int(x[0]), x[1], x[2]), lines))
        return lines


class OrderRepo(DataRepo):
    def __init__(self, file: str):
        DataRepo.__init__(self, file)
        self.orders = []
        if os.path.exists(self.file):
            self.load()
        self.orders = self.list

    @staticmethod
    def convert_to_string(ord: list):
        return functools.reduce(lambda a, b: a + b, map(lambda x: str(x) + '\n', ord))

    @staticmethod
    def convert_from_string(s: str):
        lines = s.split('\n')
        lines = [x.split(', ') for x in lines]
        lines.pop(-1)
        lines = list(map(lambda x: Bestellung(int(x[0]), int(x[1]), list(x[2]), list(x[3]), float(x[4])), lines))
        return lines
