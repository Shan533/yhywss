class Actor:
    def __init__(self, fisrtname, lastname):
        self.firstname = fisrtname
        self.lastname = lastname

    def __str__(self):
        return "{} {}" .format(self.firstname, self.lastname)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            return self.firstname == other.firstname and \
                   self.lastname == other.lastname
