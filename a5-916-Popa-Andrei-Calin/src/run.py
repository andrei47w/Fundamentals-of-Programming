"""
    A5 / Problem 3


    Manage a list of students. Each student has an id (integer, unique), a name (string) and a group (positive integer).
Provide the following features:

1    Add a student. Student data is read from the console.
2    Display the list of students.
3    Filter the list so that students in a given group (read from the console) are deleted from the list.
4    Undo the last operation that modified program data. This step can be repeated.


"""

from tests.tests import test_all
from ui.console import UI

if __name__ == '__main__':
    test_all()

    ui = UI()
    # ui.list_student_ui()
    ui.start()
