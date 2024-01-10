from repo.studrepo import StudRepo


class Controller:
    def __init__(self, repo: StudRepo):
        self.repo = repo

    def sort_stud(self):
        return sorted(self.repo.students)

    def filter_by_street(self, street):
        return [stud for stud in self.repo.students if stud.address.street == street]