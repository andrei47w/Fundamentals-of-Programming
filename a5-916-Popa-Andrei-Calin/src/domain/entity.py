class Student:
    def __init__(self, id_, name, group):
        self._id = id_
        self._name = name
        self._group = group

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

  #  def __add__(self, other):
  #      return self

    def __str__(self):
        return 'ID: ' + str(self.id) + '      name: ' + self.name + '     group: ' + str(self._group)
