from logic.logic import Controller
from entities.student import Student, Address


class Console:
    def __init__(self, ctr: Controller):
        self.ctr = ctr

    def menu(self):
        return """
        1 - Add Student
        2 - Sort Student
        3 - Filter by Street
        4 - Exit
        """

    def run(self):
        while True:
            print(self.menu())
            opt = int(input('Option: '))
            if opt == 1:
                name = input('Name: ')
                street = input('Street: ')
                nr = int(input('Nr: '))
                self.ctr.repo.add(Student(name, Address(street=street, nr=nr)))

            if opt == 2:
                students = self.ctr.sort_stud()
                for stud in students:
                    print(stud)

            if opt == 3:
                street = input('Street: ')
                students = self.ctr.filter_by_street(street)
                for stud in students:
                    print(stud)

            if opt == 4:
                break
