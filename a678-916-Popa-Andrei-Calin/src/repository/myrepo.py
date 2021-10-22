from random import randrange

import names

from src.domain.entities import Person, Activity


class Repository:
    def __init__(self):
        self._persons = []
        self._activities = []
        desc = ['football', 'homework', 'sleeping', 'gym', 'shopping', 'watching movies', 'hiking', 'jogging',
                'studying']
        for i in range(1, 10):
            # generates random person
            name = names.get_full_name()
            id = i
            phone_number = '07'
            phone_number += str(randrange(10000000, 99999999))
            self._persons.append(Person(id, name, phone_number))

            # generates random activity
            act_pers_list = []
            random_nr = randrange(1, 5)
            for j in range(random_nr):
                if j != 0:
                    try:
                        act_pers_list.append(randrange(act_pers_list[-1] + 1, 11))
                    except:
                        break
                else:
                    act_pers_list.append(randrange(1, 10))
            date = str(randrange(1, 29)) + '/' + str(randrange(1, 12)) + '/' + '2020'
            time = str(randrange(1, 23))
            time += '/' + str(randrange(int(time) + 1, 25))
            self._activities.append(Activity(id, act_pers_list, date, time, desc[randrange(8)]))
        self._persons.append(Person(10, 'Rick Astley', '0740129812'))
        self._activities.append(Activity(10, [10], '23/8/2020', '12/13', 'rickrolling'))

    def p_add(self, pers_id, name, phone_number):
        self._persons.append(Person(pers_id, name, phone_number))

    def p_remove(self, pers_id):
        for person in self._persons:
            if person.pers_id == pers_id:
                self._persons.remove(person)
                return

    def p_storage(self):
        """
        Returns the list of current persons
        """
        return self._persons

    def a_add(self, act_id, pers_list, date, time, desc):
        self._activities.append(Activity(act_id, pers_list, date, time, desc))

    def a_remove(self, act_id):
        for activity in self._activities:
            if activity.act_id == act_id:
                self._activities.remove(activity)
                return

    def a_storage(self):
        """
        Returns the list of current activities
        """
        return self._activities

    def p_sort(self):
        """
        Sorts the persons
        """
        self._persons.sort(key=lambda person: person.pers_id)

    def a_sort(self):
        """
        Sorts the activities
        """
        self._activities.sort(key=lambda activity: activity.act_id)
