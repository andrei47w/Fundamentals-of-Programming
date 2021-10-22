from services.service import Service


class UI:
    def __init__(self):
        self._service = Service()

    def show_menu(self):
        """
        Prints menu
        """
        print("\n\n         MENU:\n"
              "1:      Add a student. Student data is read from the console.\n"
              "2:      Display the list of students.\n"
              "3:      Filter the list so that students in a given group (read from the console) are deleted from the list.\n"
              "4:      Undo the last operation that modified program data. This step can be repeated.\n"
              "0:      Exit")

    def read_input(self):
        """
        Reads the input, returning the command
        """
        command = input('   Enter command: ')
        return command

    def read_student_ui(self):
        """
        Reads id, name and group returning them
        """
        id = int(input('Enter student id: '))
        name = input('Enter student name: ')
        group = int(input('Enter student group: '))
        return [id, name, group]

    def add_student_ui(self):
        """
        Adds the new student to the list
        """
        param = self.read_student_ui()
        self._service.add(*param)

    def list_student_ui(self):
        """
        Lists all students saved
        """
        student_list = self._service.storage()
        for student in student_list:
            print(str(student))

    def filter_student_list(self):
        """
        Filters students by their groups using the function found in service
        """
        group = int(input('Enter group: '))
        self._service.filter(group)

    def undo_ui(self):
        """
        Undos the last operation which made any changes in the students list using the function found in service
        """
        self._service.undo()

    def start(self):
        """
        Starts the command based menu, looping it
        """
        while True:
            try:
                self.show_menu()
                command = self.read_input()
                if command == '1':
                    self.add_student_ui()
                elif command == '0':
                    exit("Bye!")
                elif command == '2':
                    self.list_student_ui()
                elif command == '3':
                    self.filter_student_list()
                elif command == '4':
                    self.undo_ui()
                else:
                    raise ValueError('Invalid command ')
            except ValueError as ve:
                print(str(ve))
