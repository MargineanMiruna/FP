import pickle
import os

class StudRepo:
    def __init__(self):
        self.students = []

    def add(self, stud):
        self.students.append(stud)

    def find(self, name):
        for stud in self.students:
            if stud.name == name:
                return stud
        return None


class FileStudRepo(StudRepo):
    def __init__(self, filename):
        StudRepo.__init__(self)
        self.filename = filename
        if os.path.exists(self.filename):
            self.load()

    def save(self):
        f = open(self.filename, 'ab')
        pickle.dump(self.students, f)
        f.close()

    def add(self, stud):
        super().add(stud)
        self.save()

    def load(self):
        f = open(self.filename, 'rb')
        self.students = pickle.load(f)
        f.close()

