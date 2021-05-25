class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, photo, song):
        self.first = first
        self.last = last
        self.photo = photo
        self.song = song

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', '{}', {})".format(self.first, self.last, self.photo, self.song)
        #return "Employee('{}', '{}', {})".format(self.first, self.last, self.photo)


