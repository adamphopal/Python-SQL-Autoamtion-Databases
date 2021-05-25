class Bruin:
    """A sample Bruin class"""

    def __init__(self, first, last, username):
        self.first = first
        self.last = last
        self.username = username

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Bruin('{}', '{}', {})".format(self.first, self.last, self.username)
