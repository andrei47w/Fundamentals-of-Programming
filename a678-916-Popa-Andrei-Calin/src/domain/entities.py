from dataclasses import dataclass


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
