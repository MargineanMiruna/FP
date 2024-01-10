from logic.logic import Controller
from repo.studrepo import StudRepo, FileStudRepo
from ui.console import Console


def main():
    print('Which Repo?\n1 - Memory\n2 - File')
    wahl = int(input())
    if wahl == 1:
        repo = StudRepo()
    else:
        repo = FileStudRepo('stud.data')

    c = Console(Controller(repo))
    c.run()


main()
