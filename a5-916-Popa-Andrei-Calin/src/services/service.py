from domain.entity import Student
from random import randrange

import names


class Service:
    def __init__(self):
        """
        Creates the initial random student list
        """
        self._students = []
        self._history = []
        for i in range(1, 11):
            name = names.get_full_name()
            id = i
            group = randrange(30)
            self._students.append(Student(id, name, group))

    def add_history(self):
        """
        Adds the student list to history before it gets changed my the next operation
        """
        self._history.append(self._students[:])

    def validate(self, id, group):
        """
        Checks if student's id and group are valid, returning an error
        """
        for student in self._students:
            if student.id == id:
                raise ValueError("  Id is not unique")
        if type(group) != int or group < 0:
            raise ValueError("  Group is not a positive integer")

    def add(self, id, name, group):
        """
        Adds a new student to the list, validating the parameters and adding the old list to history
        """
        self.validate(id, group)
        self.add_history()
        self._students.append(Student(id, name, group))

    def storage(self):
        """
        Returns the current list
        """
        return self._students

    def filter(self, arggroup):
        """
        Filters students by their groups
        """
        self.add_history()
        for student in self._students[:]:
            if student.group == arggroup:
                self._students.remove(student)

    def __len__(self):
        """
        Returns list's length
        """
        return len(self._students)

    def undo(self):
        """
        Undos the last operation which made any changes in the students list
        """
        if len(self._history) == 0:
            raise ValueError('  Nothing left to undo')
        self._students = self._history[-1]
        self._history.pop()
