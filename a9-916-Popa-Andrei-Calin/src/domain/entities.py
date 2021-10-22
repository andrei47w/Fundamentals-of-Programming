from dataclasses import dataclass
import pickle

@dataclass
class Person:
    __pers_id: int
    __name: str
    __phone_number: str

    @property
    def pers_id(self):
        return self.__pers_id

    @property
    def name(self):
        return self.__name

    @property
    def phone_number(self):
        return self.__phone_number

    def __str__(self):
        string = str(self.__pers_id)
        for i in range(1, 20 - len(str(self.__pers_id))):
            string += ' '
        string += self.__name
        for i in range(1, 30 - len(self.__name)):
            string += ' '
        string += str(self.__phone_number)
        return string
        """
        return 'ID: ' + str(self.__pers_id) + '      name: ' + self.__name + '     phone number: ' + str(
            self.__phone_number)
        """

def write_person_text_file(file_name, persons):
    f = open(file_name, "w")
    try:
        for p in persons:
            person_str = str(p.pers_id) + ";" + p.name + ";" + p.phone_number + "\n"
            f.write(person_str)
        f.close()
    except Exception as e:
        print("An error occurred - " + str(e))

def read_person_text_file(file_name):
    result = []
    try:
        f = open(file_name, "r")
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split(";")
            result.append(Person(int(line[0]), line[1], line[2]))
            line = f.readline().strip()
        f.close()
    except IOError as e:
        print("An error occurred - " + str(e))
        raise e

    return result

def write_person_binary_file(file_name, persons):
    f = open(file_name, "wb")
    pickle.dump(persons, f)
    f.close()

def read_person_binary_file(file_name):
    result = []
    try:
        f = open(file_name, "rb")
        return pickle.load(f)
    except EOFError:
        return []
    except IOError as e:
        print("An error occurred - " + str(e))
        raise e

    return result


@dataclass
class Activity:
    __act_id: int
    __pers_list: list
    __date: str
    __time: str
    __desc: str

    @property
    def act_id(self):
        return self.__act_id

    @property
    def act_pers_list(self):
        return self.__pers_list

    @property
    def date(self):
        return self.__date

    @property
    def time(self):
        return self.__time

    @property
    def desc(self):
        return self.__desc

    def __str__(self):
        string = str(self.__act_id)
        for i in range(1, 20 - len(str(self.__act_id))):
            string += ' '
        string += str(self.__pers_list)
        for i in range(1, 20 - len(str(self.__pers_list))):
            string += ' '
        string += self.__date
        for i in range(1, 20 - len(self.__date)):
            string += ' '
        string += self.__time[:self.__time.find('/')] + ':00 -> ' + self.__time[self.__time.find('/') + 1:] + ':00'
        for i in range(1, 20 - len(
                self.__time[:self.__time.find('/')] + ':00 -> ' + self.__time[self.__time.find('/') + 1:] + ':00')):
            string += ' '
        string += self.__desc
        return string
        """
        return 'ID: ' + str(self.__act_id) + \
               '       persons: ' + str(self.__pers_list) + \
               '       date:' + self.__date + \
               '       time: ' + self.__time[:self.__time.find('/')] + ':00 -> ' + \
               self.__time[self.__time.find('/') + 1:] + ':00' + \
               '       description: ' + self.__desc
        """

def write_activity_text_file(file_name, activities):
    f = open(file_name, "w")
    try:
        for a in activities:
            activity_str = str(a.act_id) + ";" + str(a.act_pers_list) + ";" + a.date + ';' + a.time + ';' + a.desc + "\n"
            f.write(activity_str)
        f.close()
    except Exception as e:
        print("An error occurred - " + str(e))

def read_activity_text_file(file_name):
    result = []
    try:
        f = open(file_name, "r")
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split(";")
            pers_list = line[1]
            result.append(Activity(int(line[0]), pers_list, line[2], line[3], line[4]))
            line = f.readline().strip()
        f.close()
    except IOError as e:
        print("An error occurred - " + str(e))
        raise e

    return result

def write_activity_binary_file(file_name, activity):
    f = open(file_name, "wb")
    pickle.dump(activity, f)
    f.close()

def read_activity_binary_file(file_name):
    result = []
    try:
        f = open(file_name, "rb")
        return pickle.load(f)
    except EOFError:
        return []
    except IOError as e:
        print("An error occurred - " + str(e))
        raise e

    return result